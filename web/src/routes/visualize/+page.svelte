<script lang="ts">
	import Layout from '../../lib/Layout.svelte';
	import { apiClient } from '../../lib/api.ts';
	import { onMount } from 'svelte';

	let fileInput: HTMLInputElement;
	let uploading = false;
	let uploadError = '';
	let plans: any[] = [];

	onMount(async () => {
		try {
			plans = await apiClient.getPlans();
		} catch (error) {
			console.error('Failed to load plans:', error);
		}
	});

	async function handleFileUpload() {
		const file = fileInput?.files?.[0];
		if (!file) return;

		uploading = true;
		uploadError = '';

		try {
			const plan = await apiClient.uploadPlan(file);
			plans = [...plans, plan];
			fileInput.value = '';
		} catch (error) {
			uploadError = error instanceof Error ? error.message : 'Upload failed';
		} finally {
			uploading = false;
		}
	}

	async function deletePlan(id: string) {
		try {
			await apiClient.deletePlan(id);
			plans = plans.filter(p => p.id !== id);
		} catch (error) {
			console.error('Failed to delete plan:', error);
		}
	}
</script>

<Layout>
	<div class="visualize-page">
		<h1>Visualize Terraform Plans</h1>
		<p>Upload your Terraform plan files to generate infrastructure diagrams.</p>

		<div class="upload-section">
			<h2>Upload New Plan</h2>
			<div class="upload-form">
				<input
					bind:this={fileInput}
					type="file"
					accept=".json,.tfplan"
					disabled={uploading}
				/>
				<button on:click={handleFileUpload} disabled={uploading}>
					{uploading ? 'Uploading...' : 'Upload Plan'}
				</button>
			</div>
			
			{#if uploadError}
				<div class="error-message">
					{uploadError}
				</div>
			{/if}
		</div>

		<div class="plans-section">
			<h2>Uploaded Plans</h2>
			
			{#if plans.length === 0}
				<div class="no-plans">
					<p>No plans uploaded yet. Upload a Terraform plan file to get started.</p>
				</div>
			{:else}
				<div class="plans-grid">
					{#each plans as plan}
						<div class="plan-card">
							<h3>{plan.name}</h3>
							<p>Resources: {plan.resources?.length || 0}</p>
							<p>Created: {new Date(plan.created_at).toLocaleDateString()}</p>
							<div class="plan-actions">
								<button class="btn-primary">View Diagram</button>
								<button class="btn-secondary" on:click={() => deletePlan(plan.id)}>
									Delete
								</button>
							</div>
						</div>
					{/each}
				</div>
			{/if}
		</div>
	</div>
</Layout>

<style>
	.visualize-page {
		max-width: 800px;
		margin: 0 auto;
	}

	.upload-section {
		background: #f8f9fa;
		padding: 2rem;
		border-radius: 8px;
		margin: 2rem 0;
	}

	.upload-form {
		display: flex;
		gap: 1rem;
		align-items: center;
		margin-top: 1rem;
	}

	.upload-form input[type="file"] {
		flex: 1;
	}

	.upload-form button {
		padding: 0.75rem 1.5rem;
		background: #007bff;
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	.upload-form button:disabled {
		background: #6c757d;
		cursor: not-allowed;
	}

	.error-message {
		color: #dc3545;
		margin-top: 1rem;
		padding: 0.75rem;
		background: #f8d7da;
		border: 1px solid #f5c6cb;
		border-radius: 4px;
	}

	.plans-section {
		margin: 2rem 0;
	}

	.no-plans {
		text-align: center;
		color: #6c757d;
		padding: 2rem;
		background: #f8f9fa;
		border-radius: 8px;
	}

	.plans-grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
		gap: 1rem;
		margin-top: 1rem;
	}

	.plan-card {
		background: white;
		border: 1px solid #dee2e6;
		border-radius: 8px;
		padding: 1.5rem;
		box-shadow: 0 2px 4px rgba(0,0,0,0.1);
	}

	.plan-card h3 {
		margin: 0 0 1rem 0;
		color: #495057;
	}

	.plan-card p {
		margin: 0.5rem 0;
		color: #6c757d;
		font-size: 0.875rem;
	}

	.plan-actions {
		display: flex;
		gap: 0.5rem;
		margin-top: 1rem;
	}

	.btn-primary {
		background: #007bff;
		color: white;
		border: none;
		padding: 0.5rem 1rem;
		border-radius: 4px;
		cursor: pointer;
		font-size: 0.875rem;
	}

	.btn-secondary {
		background: #6c757d;
		color: white;
		border: none;
		padding: 0.5rem 1rem;
		border-radius: 4px;
		cursor: pointer;
		font-size: 0.875rem;
	}

	.btn-primary:hover {
		background: #0056b3;
	}

	.btn-secondary:hover {
		background: #545b62;
	}
</style>