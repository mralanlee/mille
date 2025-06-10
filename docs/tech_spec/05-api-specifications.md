# 5. API Specifications

## 5.1 Webhook API

Endpoint: `/api/webhook/plan`
Method: POST
 Payload:
```json
{
  "project": "my-project",
  "environment": "production",
  "pullRequestId": "123",
  "commitSha": "abc123",
  "planJson": "...", // The JSON plan content or a URL to it
  "metadata": {
    "initiatedBy": "username",
    "timestamp": "2025-06-07T12:00:00Z",
    "cwd": "/path/to/terraform/config",
    "terraformVersion": "1.5.2",
    "repositoryName": "org/repo-name",
    "tags": ["networking", "production", "us-west", "monthly-update"]
  }
}
```

Response:

```json
{
  "status": "success",
  "visualizationUrl": "http://visualization-server/view/12345",
  "summary": {
    "create": 5,
    "update": 2,
    "delete": 1,
    "recreate": 1
  }
}
```

## 5.2 CLI Interface

### Dual-CLI Usage

#### Go CLI (Parsing)
```bash
# Parse Terraform plan to structured JSON
mille --input plan.json --output parsed.json

# Parse with YAML output format
mille --input plan.json --format yaml --output plan.yaml

# Parse with validation
mille --input plan.json --output parsed.json --validate
```

#### Python CLI (Visualization)
```bash
# Generate diagram from parsed data
mille --input parsed.json --output diagram.svg

# Generate with specific format and theme
mille --input parsed.json --format png --theme aws --output diagram.png

# Generate interactive HTML
mille --input parsed.json --format html --output interactive.html
```

### Container Interface (Unified)

```bash
# Two-step process via container
docker run mille parse --input plan.json --output parsed.json
docker run mille diagram --input parsed.json --output diagram.svg

# Single command with chaining (future)
docker run mille --input plan.json --output diagram.svg

# CI/CD integration
docker run -v $(pwd):/workspace mille parse --input /workspace/plan.json --output /workspace/parsed.json
docker run -v $(pwd):/workspace mille diagram --input /workspace/parsed.json --output /workspace/diagram.svg
```

## 5.3 Inter-Service Data Format

### Parsed Plan JSON Schema
```json
{
  "version": "1.0",
  "terraform_version": "1.5.2",
  "resources": [
    {
      "address": "aws_instance.web",
      "type": "aws_instance",
      "provider": "aws",
      "change": {
        "action": "create",
        "before": null,
        "after": {
          "instance_type": "t3.small",
          "ami": "ami-12345678"
        }
      }
    }
  ],
  "metadata": {
    "timestamp": "2025-06-10T03:47:00Z",
    "parsed_by": "mille-go",
    "version": "1.0.0"
  }
}
```

