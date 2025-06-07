# Mille Project Context

## Project Overview
Mille is a Terraform/OpenTofu plan visualization tool that creates infrastructure diagrams from plan files.

## Technology Stack
- **Backend**: Go 1.18+ (CLI and API server)
- **Visualization**: Python with `diagrams` library
- **Web UI**: Svelte
- **Dependencies**: Graphviz

## Project Structure
```
mille/
├── cmd/mille/          # CLI entry point
├── internal/           # Go internal packages
│   ├── parser/         # TF plan parsing
│   ├── render/         # Rendering logic
│   └── server/         # HTTP server
├── python/             # Python visualization
├── web/                # Svelte web UI
│   └── src/
│       ├── components/
│       ├── lib/
│       └── routes/
├── tests/              # Test files
│   ├── unit/
│   └── integration/
├── scripts/            # Build and utility scripts
└── docs/               # Documentation
    └── tech_spec/      # Technical specifications
```

## Development Commands
- **Go**: `go mod init github.com/user/mille` (adjust repo path)
- **Python**: `python -m venv venv && source venv/bin/activate`
- **Web**: `cd web && npm init -y && npm install svelte`
- **Build**: `make build` (once Makefile is created)
- **Test**: `make test`

## Key Features
1. Parse Terraform/OpenTofu plan JSON files
2. Generate infrastructure diagrams using Python diagrams library
3. Provide web UI for interactive visualization
4. Support multiple cloud providers (AWS, Azure, GCP)
5. Enable customizable layouts and theming

## Important Notes
- The project is in initial setup phase
- Follow Go module conventions
- Use Python virtual environment for isolation
- Svelte app should be SPA with TypeScript support
- All visualization logic should be in Python, not Go