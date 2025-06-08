<script lang="ts">
	// Layout component for consistent page structure
</script>

<div class="app">
	<header>
		<nav>
			<div class="nav-brand">
				<h1>Mille</h1>
				<span class="tagline">Terraform Plan Visualizer</span>
			</div>
			<div class="nav-links">
				<a href="/">Home</a>
				<a href="/visualize">Visualize</a>
				<a href="/about">About</a>
			</div>
		</nav>
	</header>

	<main>
		<slot />
	</main>

	<footer>
		<p>&copy; 2024 Mille - Infrastructure Visualization Tool</p>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	header {
		background-color: #f8f9fa;
		border-bottom: 1px solid #dee2e6;
		padding: 1rem 0;
	}

	nav {
		display: flex;
		justify-content: space-between;
		align-items: center;
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 1rem;
	}

	.nav-brand h1 {
		margin: 0;
		color: #ff3e00;
		font-size: 1.5rem;
	}

	.nav-brand .tagline {
		font-size: 0.8rem;
		color: #6c757d;
		display: block;
	}

	.nav-links {
		display: flex;
		gap: 1rem;
	}

	.nav-links a {
		color: #495057;
		text-decoration: none;
		padding: 0.5rem 1rem;
		border-radius: 4px;
		transition: background-color 0.2s;
	}

	.nav-links a:hover {
		background-color: #e9ecef;
	}

	main {
		flex: 1;
		max-width: 1200px;
		margin: 0 auto;
		padding: 2rem 1rem;
		width: 100%;
	}

	footer {
		background-color: #f8f9fa;
		border-top: 1px solid #dee2e6;
		padding: 1rem;
		text-align: center;
		color: #6c757d;
		font-size: 0.875rem;
	}

	footer p {
		margin: 0;
	}
</style>