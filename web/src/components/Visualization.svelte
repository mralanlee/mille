<script lang="ts">
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  
  let svgElement: SVGSVGElement;
  let containerElement: HTMLDivElement;

  // Example data structure for Terraform resources
  interface TerraformResource {
    id: string;
    type: string;
    name: string;
    provider: string;
    dependencies: string[];
  }

  // Sample data for demonstration
  const sampleData: TerraformResource[] = [
    {
      id: "aws_vpc.main",
      type: "aws_vpc",
      name: "main",
      provider: "aws",
      dependencies: []
    },
    {
      id: "aws_subnet.public",
      type: "aws_subnet", 
      name: "public",
      provider: "aws",
      dependencies: ["aws_vpc.main"]
    },
    {
      id: "aws_instance.web",
      type: "aws_instance",
      name: "web", 
      provider: "aws",
      dependencies: ["aws_subnet.public"]
    }
  ];

  onMount(() => {
    if (svgElement && containerElement) {
      createVisualization();
    }
  });

  function createVisualization() {
    // Clear previous content
    d3.select(svgElement).selectAll("*").remove();

    const width = containerElement.clientWidth;
    const height = 400;

    const svg = d3.select(svgElement)
      .attr("width", width)
      .attr("height", height);

    // Create a simple node-link diagram
    const nodes = sampleData.map(d => ({ ...d }));
    const links = sampleData.flatMap(d => 
      d.dependencies.map(dep => ({
        source: dep,
        target: d.id
      }))
    );

    // Create force simulation
    const simulation = d3.forceSimulation(nodes)
      .force("link", d3.forceLink(links).id((d: any) => d.id).distance(100))
      .force("charge", d3.forceManyBody().strength(-300))
      .force("center", d3.forceCenter(width / 2, height / 2));

    // Create links
    const link = svg.append("g")
      .selectAll("line")
      .data(links)
      .enter().append("line")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
      .attr("stroke-width", 2);

    // Create nodes
    const node = svg.append("g")
      .selectAll("circle")
      .data(nodes)
      .enter().append("circle")
      .attr("r", 20)
      .attr("fill", getNodeColor)
      .attr("stroke", "#fff")
      .attr("stroke-width", 2);

    // Add labels
    const label = svg.append("g")
      .selectAll("text")
      .data(nodes)
      .enter().append("text")
      .text((d: any) => d.name)
      .attr("font-size", "12px")
      .attr("text-anchor", "middle")
      .attr("dy", 4);

    // Update positions on tick
    simulation.on("tick", () => {
      link
        .attr("x1", (d: any) => d.source.x)
        .attr("y1", (d: any) => d.source.y)
        .attr("x2", (d: any) => d.target.x)
        .attr("y2", (d: any) => d.target.y);

      node
        .attr("cx", (d: any) => d.x)
        .attr("cy", (d: any) => d.y);

      label
        .attr("x", (d: any) => d.x)
        .attr("y", (d: any) => d.y);
    });

    // Add drag behavior
    node.call(d3.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended));

    function dragstarted(event: any, d: any) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event: any, d: any) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event: any, d: any) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
  }

  function getNodeColor(d: TerraformResource) {
    // Color nodes based on resource type
    switch (d.provider) {
      case 'aws': return '#ff9900';
      case 'azure': return '#0078d4';
      case 'gcp': return '#4285f4';
      default: return '#6c757d';
    }
  }

  // Handle window resize
  function handleResize() {
    if (containerElement && svgElement) {
      createVisualization();
    }
  }
</script>

<svelte:window on:resize={handleResize} />

<div class="visualization-wrapper" bind:this={containerElement}>
  <div class="visualization-header">
    <h3>Infrastructure Diagram</h3>
    <p>Interactive visualization of Terraform resources and their dependencies</p>
  </div>
  
  <div class="visualization-content">
    <svg bind:this={svgElement}></svg>
  </div>
  
  <div class="visualization-info">
    <p>This is a demonstration visualization. In production, this would render actual Terraform plan data.</p>
  </div>
</div>

<style>
  .visualization-wrapper {
    width: 100%;
    background: #f8f9fa;
    border-radius: 8px;
    padding: 1rem;
  }

  .visualization-header {
    margin-bottom: 1rem;
  }

  .visualization-header h3 {
    margin: 0 0 0.5rem 0;
    color: #495057;
  }

  .visualization-header p {
    margin: 0;
    color: #6c757d;
    font-size: 0.875rem;
  }

  .visualization-content {
    background: white;
    border-radius: 4px;
    border: 1px solid #dee2e6;
  }

  .visualization-info {
    margin-top: 1rem;
    font-size: 0.75rem;
    color: #6c757d;
    font-style: italic;
  }

  .visualization-info p {
    margin: 0;
  }
</style>