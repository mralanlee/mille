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

```bash
# Basic usage
mille plan.json --output=diagram.svg

# Web server upload
mille plan.json --server=http://visualization-server

# Start local preview server
mille plan.json --serve
```

