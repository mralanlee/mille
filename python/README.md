# Mille Visualization (`mille_viz`)

The Python visualization component for Mille - a Terraform/OpenTofu plan visualization tool that creates infrastructure diagrams from plan files.

## Purpose

`mille_viz` is responsible for generating beautiful infrastructure diagrams from Terraform plan data. It bridges the gap between raw Terraform JSON output and visual representations that are easy to understand and share.

### Key Features

- **Multi-Provider Support**: AWS, Azure, and GCP cloud providers
- **Terraform Plan Parsing**: Direct integration with Terraform JSON plan files
- **Professional Diagrams**: Uses the `diagrams` library for high-quality output
- **Extensible Architecture**: Easy to add new providers and resource types
- **Clean API**: Simple interface for Go CLI integration

## Architecture

```
mille_viz/
├── __init__.py           # Package exports
├── renderer.py           # DiagramRenderer class - core visualization logic
└── utils.py             # Utility functions for parsing and validation
```

### Core Components

1. **DiagramRenderer** (`renderer.py`): Main class that converts Terraform plan data into visual diagrams
2. **Utility Functions** (`utils.py`): Helper functions for parsing Terraform plans and extracting resource information
3. **Test Suite** (`test_diagrams.py`): Validation script to ensure the environment is working correctly

## How It Works

1. **Parse Terraform Plan**: Read and validate Terraform JSON plan files
2. **Extract Resources**: Identify infrastructure resources and their relationships
3. **Map to Diagrams**: Convert Terraform resource types to appropriate diagram components
4. **Generate Visualization**: Create PNG diagrams using the `diagrams` library
5. **Output**: Save diagrams to specified locations for display or embedding

### Supported Resource Types

#### AWS
- `aws_instance` → EC2 instances
- `aws_db_instance` → RDS databases
- `aws_vpc` → VPC networks
- `aws_subnet` → Subnets

#### Azure
- `azurerm_virtual_machine` → Virtual Machines
- `azurerm_sql_database` → SQL Databases

#### GCP
- `google_compute_instance` → Compute Engine
- `google_sql_database_instance` → Cloud SQL

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Graphviz system library

#### Install Graphviz

**macOS:**
```bash
brew install graphviz
```

**Ubuntu/Debian:**
```bash
sudo apt-get install graphviz
```

**Windows:**
Download from [Graphviz website](https://graphviz.org/download/) or use Chocolatey:
```bash
choco install graphviz
```

### Installation Methods

#### Option 1: Development Installation (Recommended)

For development or when integrating with the Go CLI:

```bash
cd python/
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

This installs the package in "editable" mode, so changes to the code are immediately available.

#### Option 2: Requirements Only

If you prefer not to install as a package:

```bash
cd python/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Note: With this approach, you'll need to manage PYTHONPATH manually when importing `mille_viz`.

### Verify Installation

Run the test script to ensure everything is working:

```bash
cd python/
python test_diagrams.py
```

Expected output:
```
✓ Basic diagram test passed - Diagrams library is working!
✓ Mille visualization module import test passed!
✓ DiagramRenderer for aws created successfully!
✓ DiagramRenderer for azure created successfully!
✓ DiagramRenderer for gcp created successfully!
🎉 All tests passed! Python visualization environment is ready.
```

## Usage

### Basic Usage

```python
from mille_viz import DiagramRenderer, parse_tf_plan

# Parse Terraform plan
plan_data = parse_tf_plan("path/to/terraform.plan.json")

# Create renderer for AWS
renderer = DiagramRenderer(provider="aws")

# Generate diagram
output_file = renderer.render_diagram(
    plan_data=plan_data,
    output_file="my_infrastructure",
    show=False  # Set to True to display diagram immediately
)

print(f"Diagram saved to: {output_file}")
```

### Integration with Go CLI

The Go CLI will typically call this module through subprocess execution:

```go
// Example Go integration (pseudocode)
cmd := exec.Command("python", "-m", "mille_viz.renderer", 
                   "--plan", planFile, 
                   "--provider", provider,
                   "--output", outputFile)
```

### Available Functions

#### From `mille_viz.renderer`

- `DiagramRenderer(provider="aws")`: Initialize renderer for specific cloud provider
- `renderer.render_diagram(plan_data, output_file, show=False)`: Generate diagram from plan data

#### From `mille_viz.utils`

- `parse_tf_plan(file_path)`: Parse Terraform JSON plan file
- `get_supported_providers()`: Get list of supported cloud providers
- `extract_resources(plan_data)`: Extract resource information from plan
- `get_resource_dependencies(plan_data)`: Extract resource dependencies
- `validate_plan_format(plan_data)`: Validate plan data format

## Development

### Setup Development Environment

1. Clone the repository and navigate to the python directory:
```bash
cd mille/python/
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

4. Run tests to verify setup:
```bash
python test_diagrams.py
```

### Adding New Resource Types

To add support for new Terraform resource types:

1. Add the mapping in `renderer.py` in the `_get_resource_mapping()` method
2. Import the corresponding diagram component from the `diagrams` library
3. Test with a sample Terraform plan that includes the new resource

Example:
```python
# In renderer.py
from diagrams.aws.storage import S3

# In _get_resource_mapping() method for AWS:
"aws_s3_bucket": S3,
```

### Adding New Cloud Providers

1. Add provider to `supported_providers` list in `DiagramRenderer.__init__()`
2. Add new elif branch in `_get_resource_mapping()` method
3. Import required diagram components from `diagrams.{provider}`
4. Update `get_supported_providers()` in `utils.py`

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Include docstrings for all public functions and classes
- Keep functions focused and single-purpose

### Testing

Run the test suite:
```bash
python test_diagrams.py
```

For more comprehensive testing, you can create test Terraform plans and verify the output:
```python
# Create test plan data
test_plan = {
    "resource_changes": [
        {
            "type": "aws_instance",
            "name": "web_server",
            "change": {"actions": ["create"]}
        }
    ]
}

# Test rendering
renderer = DiagramRenderer("aws")
output = renderer.render_diagram(test_plan, "test_output")
```

## About setup.py

The `setup.py` file is **necessary** for this component because:

1. **Clean Imports**: Enables `from mille_viz import DiagramRenderer` from anywhere
2. **Development Workflow**: `pip install -e .` creates an editable installation
3. **Dependency Management**: Automatically installs required packages
4. **Go Integration**: Allows the Go CLI to reliably import the Python module
5. **Distribution Ready**: Enables creating wheels and distributing the package
6. **Professional Structure**: Follows Python packaging best practices

Without `setup.py`, the Go CLI would need to manage PYTHONPATH manually and imports would be fragile.

## Troubleshooting

### Common Issues

**ImportError: No module named 'diagrams'**
- Ensure you've activated the virtual environment
- Run `pip install -r requirements.txt` or `pip install -e .`

**Graphviz ExecutableNotFound**
- Install Graphviz system library (see Prerequisites)
- Ensure Graphviz is in your system PATH

**Permission denied when creating diagrams**
- Check write permissions in the output directory
- Try specifying a different output path

### Getting Help

1. Run `python test_diagrams.py` to verify environment
2. Check that Graphviz is properly installed: `dot -V`
3. Verify Python environment: `pip list` should show diagrams, graphviz, Pillow