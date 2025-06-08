# Mille

A Terraform/OpenTofu plan visualization tool that creates infrastructure diagrams from plan files.

## Overview

Mille transforms your Terraform or OpenTofu plan files into clear, visual infrastructure diagrams. It helps teams understand infrastructure changes before applying them, making it easier to review and collaborate on infrastructure as code.

## Features

- **Plan Parsing**: Parse Terraform/OpenTofu plan JSON files
- **Visual Diagrams**: Generate infrastructure diagrams using Python diagrams library
- **Web Interface**: Interactive web UI for visualization
- **Multi-Cloud Support**: Support for AWS, Azure, GCP, and other providers
- **Customizable**: Configurable layouts and theming options

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
├── tests/              # Test files
├── scripts/            # Build and utility scripts
└── docs/               # Documentation
```

## Getting Started

This project is currently in initial setup phase. Development instructions will be added as the project progresses.

## Development

### Prerequisites

- Go 1.18+
- Python 3.8+
- Node.js 16+
- Graphviz

### Setup

```bash
# Clone the repository
git clone https://github.com/mralanlee/mille.git
cd mille

# Go setup
go mod download

# Python setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Web UI setup
cd web
npm install
```

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests for any improvements.