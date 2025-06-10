# 3. System Architecture

## 3.1 High-Level Architecture
The system uses a **dual-CLI microservices architecture** consisting of:

1. **Go CLI Service**: Processes Terraform/OpenTofu plan JSON outputs and data transformation
2. **Python CLI Service**: Generates visual diagrams from processed plan data
3. **Shell Script Router**: Docker entrypoint that routes commands to appropriate CLI
4. **Web UI Service**: Svelte application for interactive visualization
5. **Container Orchestration**: Docker-based deployment for local and production use

## 3.2 Microservices Design

### Service Boundaries
- **Parse Service (Go)**: Plan parsing, validation, data transformation
- **Diagram Service (Python)**: Visualization generation, theme management
- **Web Service (Svelte)**: Interactive UI, user interface components
- **Router Service (Shell)**: Command routing, service coordination

### Communication Pattern
- **Inter-CLI**: Standardized JSON format for data exchange
- **Container-Native**: Docker volumes for file-based communication
- **API-Ready**: HTTP endpoints for future web server integration

## 3.3 Component Diagram

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Terraform     │    │  Docker          │    │   CI/CD         │
│   Plan JSON     │───▶│  Container       │◀───│   Pipeline      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                       ┌──────▼──────┐
                       │ entrypoint.sh│
                       │   (Router)   │
                       └──────┬──────┘
                              │
                    ┌─────────┼─────────┐
                    │                   │
              ┌─────▼──────┐    ┌──────▼─────┐
              │  Go CLI    │    │ Python CLI │
              │ (Parse)    │    │ (Diagram)  │
              │            │    │            │
              │ ┌────────┐ │    │ ┌────────┐ │
              │ │Parser  │ │    │ │Diagrams│ │
              │ │Logic   │ │    │ │Library │ │
              │ └────────┘ │    │ └────────┘ │
              └─────┬──────┘    └──────┬─────┘
                    │                  │
              ┌─────▼──────┐    ┌──────▼─────┐
              │ Parsed     │    │ Generated  │
              │ JSON       │───▶│ Diagram    │
              └────────────┘    └────────────┘
```

## 3.4 Data Flow

### CLI Workflow
1. **Input**: Terraform plan JSON file provided to container
2. **Routing**: `entrypoint.sh` determines operation (`parse` or `diagram`)
3. **Parse Stage**: Go CLI processes plan JSON → structured data
4. **Diagram Stage**: Python CLI processes structured data → visualization
5. **Output**: Generated diagram (SVG, PNG, HTML) or parsed JSON

### Container Orchestration Flow
1. User/CI system invokes Docker container with command
2. Shell router analyzes command and delegates to appropriate CLI
3. CLIs communicate via shared filesystem (Docker volumes)
4. Standardized JSON format ensures data compatibility
5. Output artifacts returned to host system

### Microservices Scaling (Future)
1. **Horizontal Scaling**: Python diagram service scales independently
2. **Load Balancing**: Multiple Python instances handle visualization requests
3. **Service Discovery**: Container orchestration manages service endpoints
4. **State Management**: Stateless design enables easy scaling
