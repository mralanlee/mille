# Mille Project Context

## Project Overview
Mille is a Terraform/OpenTofu plan visualization tool that creates infrastructure diagrams from plan files using a dual-CLI microservices architecture.

## Technology Stack
- **Parsing CLI**: Go 1.18+ (plan parsing and processing)
- **Visualization CLI**: Python with `diagrams` library (diagram generation)
- **Web UI**: Svelte (interactive visualization)
- **Containerization**: Docker with shell script entrypoint
- **Dependencies**: Graphviz

## Architecture Overview
Mille uses a **dual-CLI approach** with two separate `mille` executables:
- **Go CLI**: Handles Terraform plan parsing and data processing
- **Python CLI**: Handles diagram generation and visualization
- **Shell Script Router**: Docker entrypoint that routes commands to appropriate CLI
- **Microservices Design**: Each component can scale independently

## Project Structure
```
mille/
├── cmd/
│   └── mille/          # Go CLI for parsing (binary: mille)
├── internal/           # Go internal packages
│   ├── parser/         # TF plan parsing
│   └── server/         # HTTP server (if needed)
├── python/             # Python visualization package
│   └── mille_viz/      # Main Python package (includes CLI)
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
- **Python CLI**: `cd python && pip install -e . && python -m mille_viz.cli --help`
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

### Go CLI (Parsing)
```bash
mille --input plan.json --output parsed.json
mille --input plan.json --format yaml --output plan.yaml
```

### Python CLI (Visualization)
```bash
mille --input parsed.json --output diagram.svg
mille --input parsed.json --format png --theme aws --output diagram.png
```

### Container Interface (Unified)
```bash
docker run mille parse --input plan.json --output parsed.json
docker run mille diagram --input parsed.json --output diagram.svg
```

## Key Features
1. **Dual-CLI Architecture**: Separate Go parsing and Python visualization
2. **Container-Native**: Docker-first design for local and production use
3. **Microservices Ready**: Each CLI can scale independently
4. **Multi-Cloud Support**: AWS, Azure, GCP provider support
5. **Interactive Web UI**: Svelte-based visualization interface
6. **Flexible Output**: SVG, PNG, interactive HTML formats

## Important Notes
- **No Single Binary**: Each CLI is built and deployed separately
- **Docker-First**: Local development uses containers for consistency
- **Data Exchange**: Standardized JSON format between Go and Python CLIs
- **Independent Scaling**: Python visualization can scale horizontally
- **Container Orchestration**: Ready for Kubernetes deployment