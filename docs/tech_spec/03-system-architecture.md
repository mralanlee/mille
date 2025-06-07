# 3. System Architecture

## 3.1 High-Level Architecture
The system will consist of:
1. **Parser Component**: Processes Terraform/OpenTofu plan JSON outputs
2. **Visualization Engine**: Generates visual diagrams from parsed plan data
3. **CLI Interface**: Allows command-line usage for local development
4. **Web Server**: Provides persistent access to visualizations and integration with CI/CD tools

## 3.2 Component Diagram



## 3.3 Data Flow
1. Terraform plan is executed and converted to JSON
2. JSON plan is parsed by the tool
3. Visualization engine processes the parsed data
4. Output is generated (static file or web visualization)
5. For webhook integration, CI/CD systems send plans to the web server
6. Web server processes the plan and stores the visualization
7. CI/CD system receives a link to the visualization
