<script lang="ts">
  import Layout from '../lib/Layout.svelte';
  import Visualization from '../components/Visualization.svelte';
</script>

<Layout>
  <h1>Mille - Terraform Plan Visualizer</h1>
  <p>Welcome to Mille, your infrastructure visualization tool for Terraform and OpenTofu plans.</p>
  
  <div class="visualization-container">
    <Visualization />
  </div>
</Layout>

<style>
  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  .visualization-container {
    margin-top: 2rem;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
  }

  @media (min-width: 640px) {
    h1 {
      font-size: 4em;
    }
  }
</style>