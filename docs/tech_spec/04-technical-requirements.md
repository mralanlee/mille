# 4. Technical Requirements

## 4.1 Terraform/OpenTofu Compatibility
- Support for Terraform and OpenTofu versions 1.0+
- Process plans in JSON format (converted from binary `.tfplan` files)
- Handle standard resource types and modules

## 4.2 Visualization Requirements
- Represent resources as nodes in a graph
- Color-code resources based on planned actions:
  - Grey: No change
  - Orange: Update
  - Red: Destroy
  - Green: Create
  - Warning symbol for recreate actions
- Show relationships and dependencies between resources
- For web visualization: interactive features including mouseover details of changes
- Support multiple output formats: SVG, PNG, HTML

## 4.3 Web Server Requirements
- Lightweight, easy to deploy server
- Authentication mechanisms (optional)
- Webhook endpoints for CI/CD integration
- Persistent storage for visualizations
- Plan organization and searchability

## 4.4 Performance Requirements
- Process large Terraform plans (500+ resources) without excessive memory usage
- Generate visualizations within 30 seconds for typical plans
- Support concurrent webhook requests for CI/CD integration

## 4.5 Security Requirements
- Secure handling of potentially sensitive infrastructure information
- Authentication for web server access (if deployed publicly)
- No persistent storage of sensitive values from Terraform plans
