<script lang="ts">
	import Layout from '../../lib/Layout.svelte';
</script>

<Layout>
	<div class="about-page">
		<h1>About Mille</h1>
		
		<div class="intro-section">
			<p class="lead">
				Mille is a powerful visualization tool for Terraform and OpenTofu infrastructure plans,
				helping teams understand their infrastructure changes before deployment.
			</p>
		</div>

		<div class="features-section">
			<h2>Features</h2>
			<div class="features-grid">
				<div class="feature-card">
					<h3>📊 Interactive Diagrams</h3>
					<p>Generate beautiful, interactive infrastructure diagrams from your Terraform plans using D3.js visualization.</p>
				</div>
				
				<div class="feature-card">
					<h3>🔗 Dependency Mapping</h3>
					<p>Visualize resource dependencies and relationships to understand your infrastructure topology.</p>
				</div>
				
				<div class="feature-card">
					<h3>☁️ Multi-Cloud Support</h3>
					<p>Support for AWS, Azure, Google Cloud, and other major cloud providers.</p>
				</div>
				
				<div class="feature-card">
					<h3>🚀 Easy Integration</h3>
					<p>Simple CLI tool and web interface for seamless integration into your workflow.</p>
				</div>
			</div>
		</div>

		<div class="how-it-works-section">
			<h2>How It Works</h2>
			<ol class="workflow-steps">
				<li>
					<strong>Upload Your Plan:</strong> Upload your Terraform plan JSON file through the web interface or CLI.
				</li>
				<li>
					<strong>Parse Resources:</strong> Mille analyzes the plan to extract resources and their relationships.
				</li>
				<li>
					<strong>Generate Diagram:</strong> Creates interactive diagrams showing your infrastructure topology.
				</li>
				<li>
					<strong>Explore & Share:</strong> Interact with the diagram to understand dependencies and share with your team.
				</li>
			</ol>
		</div>

		<div class="technology-section">
			<h2>Technology Stack</h2>
			<div class="tech-grid">
				<div class="tech-item">
					<strong>Backend:</strong> Go 1.18+
				</div>
				<div class="tech-item">
					<strong>Frontend:</strong> SvelteKit + TypeScript
				</div>
				<div class="tech-item">
					<strong>Visualization:</strong> D3.js + Python diagrams
				</div>
				<div class="tech-item">
					<strong>Rendering:</strong> Graphviz
				</div>
			</div>
		</div>

		<div class="getting-started-section">
			<h2>Getting Started</h2>
			<p>Ready to visualize your infrastructure? Here's how to get started:</p>
			
			<div class="steps">
				<div class="step">
					<h4>1. Generate Terraform Plan</h4>
					<pre><code>terraform plan -out=plan.tfplan
terraform show -json plan.tfplan > plan.json</code></pre>
				</div>
				
				<div class="step">
					<h4>2. Upload to Mille</h4>
					<p>Use the <a href="/visualize">visualize page</a> to upload your plan.json file.</p>
				</div>
				
				<div class="step">
					<h4>3. Explore Your Infrastructure</h4>
					<p>Interactive diagrams help you understand resource relationships and dependencies.</p>
				</div>
			</div>
		</div>

		<div class="support-section">
			<h2>Support & Documentation</h2>
			<p>
				For detailed documentation, examples, and support, visit our 
				<a href="https://github.com/mralanlee/mille" target="_blank" rel="noopener">GitHub repository</a>.
			</p>
		</div>
	</div>
</Layout>

<style>
	.about-page {
		max-width: 900px;
		margin: 0 auto;
		line-height: 1.6;
	}

	.intro-section {
		margin: 2rem 0;
	}

	.lead {
		font-size: 1.125rem;
		color: #495057;
		margin: 1.5rem 0;
	}

	.features-section,
	.how-it-works-section,
	.technology-section,
	.getting-started-section,
	.support-section {
		margin: 3rem 0;
	}

	.features-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
		gap: 1.5rem;
		margin-top: 1.5rem;
	}

	.feature-card {
		background: #f8f9fa;
		padding: 1.5rem;
		border-radius: 8px;
		border: 1px solid #e9ecef;
	}

	.feature-card h3 {
		margin: 0 0 1rem 0;
		color: #495057;
		font-size: 1rem;
	}

	.feature-card p {
		margin: 0;
		color: #6c757d;
		font-size: 0.875rem;
	}

	.workflow-steps {
		padding-left: 1.5rem;
	}

	.workflow-steps li {
		margin: 1rem 0;
		color: #495057;
	}

	.workflow-steps strong {
		color: #212529;
	}

	.tech-grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
		gap: 1rem;
		margin-top: 1.5rem;
	}

	.tech-item {
		background: #e9ecef;
		padding: 1rem;
		border-radius: 4px;
		text-align: center;
		font-size: 0.875rem;
		color: #495057;
	}

	.steps {
		margin-top: 1.5rem;
	}

	.step {
		background: #f8f9fa;
		padding: 1.5rem;
		border-radius: 8px;
		margin: 1rem 0;
		border-left: 4px solid #007bff;
	}

	.step h4 {
		margin: 0 0 1rem 0;
		color: #495057;
	}

	.step p {
		margin: 0.5rem 0;
		color: #6c757d;
	}

	.step pre {
		background: #343a40;
		color: #f8f9fa;
		padding: 1rem;
		border-radius: 4px;
		overflow-x: auto;
		font-size: 0.875rem;
		margin: 1rem 0;
	}

	.step code {
		font-family: 'Courier New', monospace;
	}

	.support-section {
		background: #e7f3ff;
		padding: 2rem;
		border-radius: 8px;
		text-align: center;
	}

	.support-section a {
		color: #007bff;
		text-decoration: none;
		font-weight: 500;
	}

	.support-section a:hover {
		text-decoration: underline;
	}

	h2 {
		color: #495057;
		border-bottom: 2px solid #e9ecef;
		padding-bottom: 0.5rem;
		margin-bottom: 1.5rem;
	}
</style>