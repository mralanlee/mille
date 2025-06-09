# 15. Development Environment

## 15.1 Nix-shell Implementation

```nix
# shell.nix
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "mille-dev";
  
  buildInputs = with pkgs; [
    # Go development
    go_1_18
    gopls
    golangci-lint
    delve  # Go debugger
    
    # Python development
    python39
    python39Packages.pip
    python39Packages.venv
    python39Packages.pytest
    python39Packages.black
    python39Packages.pylint
    python39Packages.mypy
    
    # Node.js for Svelte
    nodejs-16_x
    nodePackages.npm
    nodePackages.pnpm  # Optional, faster alternative to npm
    
    # Required dependencies
    graphviz
    
    # Build tools
    gnumake
    git
  ];
  
  shellHook = ''
    # Create Python virtual environment if it doesn't exist
    if [ ! -d .venv ]; then
      echo "Creating Python virtual environment..."
      python -m venv .venv
    fi
    
    # Activate Python virtual environment
    source .venv/bin/activate
    
    # Install Python dependencies if needed
    if [ ! -f .venv/.initialized ]; then
      echo "Installing Python dependencies..."
      pip install -r python/requirements.txt
      touch .venv/.initialized
    fi
    
    # Set up GOPATH within the project
    export GOPATH=$(pwd)/.go
    export PATH=$GOPATH/bin:$PATH
    mkdir -p $GOPATH/bin
    
    # Download Go dependencies
    go mod download
    
    # Install Node.js dependencies if needed
    if [ -f web/package.json ] && [ ! -d web/node_modules ]; then
      echo "Installing Node.js dependencies..."
      (cd web && npm install)
    fi
    
    # Show environment info
    echo "🔧 mille Development Environment 🔧"
    echo "Go version: $(go version)"
    echo "Python version: $(python --version)"
    echo "Node.js version: $(node --version)"
    echo "npm version: $(npm --version)"
    echo "Graphviz version: $(dot -V 2>&1)"
    echo ""
    echo "Run 'make help' to see available commands"
  '';
  
  # Environment variables
  env = {
    GO111MODULE = "on";
    CGO_ENABLED = "1";
  };
}
```

## 15.2 Docker Development Container

```Dockerfile
FROM golang:1.18 AS go-base

# Install Go dependencies
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

# Add Python and Node.js layers
FROM go-base AS dev-environment
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    graphviz \
    make \
    git \
    curl

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# Set up Python environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY python/requirements.txt ./python/
RUN pip install -r python/requirements.txt

# Add development tools
RUN go install github.com/go-delve/delve/cmd/dlv@latest && \
    pip install pytest black mypy

# Set up workspace
WORKDIR /app
ENTRYPOINT ["/bin/bash"]
```

## 15.3 Python Dependency Management

### Requirements File Hierarchy

```
python/
├── requirements.txt          # Core dependencies for production
├── requirements-dev.txt      # Development dependencies
└── requirements-lock.txt     # Pinned dependencies for reproducibility
```

### Python Package Configuration

```
# python/pyproject.toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mille"
version = "0.1.0"
description = "Terraform Plan Visualization Tools"
readme = "README.md"
requires-python = ">=3.9"
license = {text = "Apache-2.0"}
dependencies = [
    "diagrams>=0.23.3",
    "pydantic>=1.9.0",
    "PyYAML>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.3.0",
    "pylint>=2.13.0",
    "mypy>=0.942",
]
```



