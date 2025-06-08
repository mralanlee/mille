// API utility functions for communicating with the Go backend

const API_BASE_URL = '/api';

export interface TerraformPlan {
	id: string;
	name: string;
	resources: TerraformResource[];
	created_at: string;
}

export interface TerraformResource {
	id: string;
	type: string;
	name: string;
	provider: string;
	action: 'create' | 'update' | 'delete' | 'no-op';
	dependencies: string[];
	attributes?: Record<string, any>;
}

export interface VisualizationData {
	nodes: TerraformResource[];
	edges: { source: string; target: string; }[];
}

class ApiClient {
	private async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
		const url = `${API_BASE_URL}${endpoint}`;
		
		const config: RequestInit = {
			headers: {
				'Content-Type': 'application/json',
				...options.headers
			},
			...options
		};

		try {
			const response = await fetch(url, config);
			
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			
			return await response.json();
		} catch (error) {
			console.error('API request failed:', error);
			throw error;
		}
	}

	// Upload and parse Terraform plan file
	async uploadPlan(file: File): Promise<TerraformPlan> {
		const formData = new FormData();
		formData.append('plan', file);

		const response = await fetch(`${API_BASE_URL}/plans/upload`, {
			method: 'POST',
			body: formData
		});

		if (!response.ok) {
			throw new Error(`Upload failed: ${response.statusText}`);
		}

		return await response.json();
	}

	// Get list of uploaded plans
	async getPlans(): Promise<TerraformPlan[]> {
		return this.request<TerraformPlan[]>('/plans');
	}

	// Get specific plan by ID
	async getPlan(id: string): Promise<TerraformPlan> {
		return this.request<TerraformPlan>(`/plans/${id}`);
	}

	// Generate visualization data for a plan
	async getVisualizationData(planId: string): Promise<VisualizationData> {
		return this.request<VisualizationData>(`/plans/${planId}/visualization`);
	}

	// Delete a plan
	async deletePlan(id: string): Promise<void> {
		await this.request(`/plans/${id}`, {
			method: 'DELETE'
		});
	}

	// Health check endpoint
	async healthCheck(): Promise<{ status: string; version: string }> {
		return this.request<{ status: string; version: string }>('/health');
	}
}

// Export singleton instance
export const apiClient = new ApiClient();

// Utility functions
export function formatResourceType(type: string): string {
	// Convert resource type to human-readable format
	// e.g., "aws_instance" -> "AWS Instance"
	return type
		.split('_')
		.map(word => word.charAt(0).toUpperCase() + word.slice(1))
		.join(' ');
}

export function getProviderFromResourceType(type: string): string {
	// Extract provider from resource type
	// e.g., "aws_instance" -> "aws"
	return type.split('_')[0];
}

export function getResourceIcon(type: string): string {
	// Return appropriate icon/emoji for resource type
	const provider = getProviderFromResourceType(type);
	
	switch (provider) {
		case 'aws':
			if (type.includes('instance')) return '🖥️';
			if (type.includes('vpc')) return '🔗';
			if (type.includes('subnet')) return '🏠';
			if (type.includes('security_group')) return '🛡️';
			return '☁️';
		case 'azure':
			return '🔷';
		case 'google':
		case 'gcp':
			return '🌐';
		default:
			return '📦';
	}
}