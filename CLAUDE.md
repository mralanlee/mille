# Mille Project Context

## Project Overview
Mille is a Terraform/OpenTofu plan visualization tool that creates infrastructure diagrams from plan files using a microservices architecture with a unified CLI.

## Technology Stack
- **Main CLI**: Go 1.18+ (plan parsing and orchestration)
- **Visualization Service**: Python with `diagrams` library (diagram generation)
- **Web UI**: Svelte (interactive visualization)
- **Containerization**: Docker with shell script entrypoint
- **Dependencies**: Graphviz

## Architecture Overview
Mille uses a **microservices approach** with a primary `mille` CLI and internal services:
- **Go CLI (`mille`)**: Main CLI handling Terraform plan parsing and orchestration
- **Python Visualization Library**: Internal diagram generation and visualization
- **Shell Script Router**: Docker entrypoint that routes commands to appropriate services
- **Microservices Design**: Each component can scale independently

## Project Structure
```
mille/
├── cmd/
│   └── mille/          # Main Go CLI (binary: mille)
├── internal/           # Go internal packages
│   ├── parser/         # TF plan parsing
│   ├── render/         # Rendering orchestration
│   └── server/         # HTTP server (if needed)
├── python/             # Python visualization package
│   └── mille_viz/      # Visualization library with internal CLI
├── scripts/
│   └── entrypoint.sh   # Docker container routing script
├── web/                # Svelte web UI
│   └── src/
│       ├── components/
│       ├── lib/
│       └── routes/
├── tests/              # Test files
│   ├── unit/
│   └── integration/
├── Dockerfile          # Multi-stage container build
└── docs/               # Documentation
    └── tech_spec/      # Technical specifications
```

## Development Commands

### Local Development
- **Go CLI**: `cd cmd/mille && go build -o mille`
- **Python Library**: `cd python && pip install -e .`
- **Web UI**: `cd web && npm install && npm run dev`

### Container Development
- **Build Container**: `docker build -t mille .`
- **Parse Command**: `docker run mille parse --input plan.json --output parsed.json`
- **Diagram Command**: `docker run mille diagram --input parsed.json --output diagram.svg`

### Testing
- **Go Tests**: `cd cmd/mille && go test ./...`
- **Python Tests**: `cd python && python -m pytest`
- **Integration**: `cd tests/integration && ./run_tests.sh`

## CLI Interface Design

### Main CLI (Go)
```bash
mille --input plan.json --output parsed.json
mille --input plan.json --format yaml --output plan.yaml
mille --input plan.json --output diagram.svg --format svg
mille --input plan.json --output diagram.png --format png --theme aws
```

### Container Interface (Unified)
```bash
docker run mille parse --input plan.json --output parsed.json
docker run mille diagram --input parsed.json --output diagram.svg
```

## Key Features
1. **Microservices Architecture**: Unified Go CLI with internal Python services
2. **Container-Native**: Docker-first design for local and production use
3. **Service Scalability**: Visualization services can scale independently
4. **Multi-Cloud Support**: AWS, Azure, GCP provider support
5. **Interactive Web UI**: Svelte-based visualization interface
6. **Flexible Output**: SVG, PNG, interactive HTML formats

## Important Notes
- **Unified CLI**: Single `mille` binary with internal service orchestration
- **Docker-First**: Local development uses containers for consistency
- **Data Exchange**: Standardized JSON format between Go CLI and Python services
- **Independent Scaling**: Python visualization services can scale horizontally
- **Container Orchestration**: Ready for Kubernetes deployment