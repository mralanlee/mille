# 13. Module Handling

## 13.1 Static Image Output

### Hierarchical Clustering with Smart Expansion
- Represent modules as container nodes with distinctive styling (e.g., dashed borders)
- Use a "smart expansion" algorithm that follows these rules:
  - If a module contains only unchanged resources: Collapse it by default, show as a single grey node
  - If a module contains only a few changed resources (≤3): Expand only those specific resources
  - If a module has significant changes (>3 resources): Show the module as expanded with all changed resources visible
  - If a module has critical changes (destroy operations): Always expand and highlight with warning indicators

### Visual Encoding of Module State
- Use size encoding: Larger module nodes indicate more resources inside
- Use pie chart or segmented border to show proportion of create/update/delete within the module
- Add badges or indicators showing the count of each operation type (e.g., "+5 -2 ~3")

### Multi-level Output Options
- Provide command-line options to control the expansion level:
  - `--module-depth=1`: Only show top-level modules
  - `--module-depth=2`: Show nested modules one level deep
  - `--module-depth=all`: Expand all modules
  - `--focus-changes`: Only expand modules with changes

## 13.2 Web Dashboard Output

### Interactive Module Navigation
- Implement a "focus+context" approach where:
  - Users can click a module to expand/collapse it
  - Double-click to "zoom into" a module, making it the central focus
  - Breadcrumb navigation to track hierarchy depth
  - "Back" button to return to previous view

### Progressive Disclosure
- Initially show a high-level view with only modules and critical changes
- Provide expandable details on demand
- Use transitions/animations to maintain context during expansion

### Smart Expansion Improvements
- Instead of simple expand/collapse:
  - Implement "focus mode" that highlights the selected module and dims others
  - Add "fish-eye" effect that expands the module under cursor while keeping others visible
  - Provide "related resources" view that shows only connected resources

### Resource Grouping Controls
- Let users toggle between:
  - Strict module hierarchy (resources grouped by modules)
  - Flat view (all resources visible)
  - Functional grouping (by resource type or service)
  - Change-based grouping (all creates together, etc.)

## 13.3 Fallback Strategies

### Mermaid Diagram Fallback

When the number of nodes exceeds a rendering threshold for static image generation, the tool automatically falls back to generating Mermaid diagrams in Markdown format:

```Mermaid
flowchart TD
    %% Style definitions
    classDef create fill:#28a745,color:#fff,stroke:#23903c,stroke-width:2px
    classDef update fill:#fd7e14,color:#fff,stroke:#d8690f,stroke-width:2px
    classDef destroy fill:#dc3545,color:#fff,stroke:#bd2130,stroke-width:2px
    classDef recreate fill:#ffc107,color:#000,stroke:#d39e00,stroke-width:2px,stroke-dasharray: 5 5
    classDef nochange fill:#6c757d,color:#fff,stroke:#5a6268,stroke-width:1px
    
    %% Resources
    vpc["aws_vpc.main"]
    subnet1["aws_subnet.public_1"]
    subnet2["aws_subnet.public_2"]
    igw["aws_internet_gateway.main"]
    route["aws_route_table.public"]
    
    %% Relationships
    vpc --> subnet1
    vpc --> subnet2
    vpc --> igw
    igw --> route
    
    %% Apply styles based on actions
    vpc:::create
    subnet1:::create
    subnet2:::create
    igw:::update
    route:::nochange
```

This generates a diagram like this when rendered by Markdown viewers that support Mermaid:

![Example Mermaid Diagram](https://mermaid.ink/img/pako:eNp1kMFqwzAMhl9F-NSD9QG8QwsLbCu0F98UWVZjFtkKtgNrybt3Sf9QRnczy_q-X7JmDpBDBpbWJ3FoURxPEjyNaLz0KNZVUz9v6k19R08jwsObXaIQYkB3NlIGQmXeglzRzE_y_LRFS3xF__VOB3HVTB1HGn_ckQsxk_o6TJGHZbDZi2XsJcYFgyRarELZQ_b8Nxb2XUY5H_qb3IGzldQRoEpXi8LQ5dpHXP7R0ib87FQG1B90aS-NQJfOT-_PsBwwO9LQwfQb2OQ1hvHWofYpzN6GTrI_fE2NeTnk36-qXFXNvobyF9KNajE?type=png)

#### Implementation Approach

- Generate Mermaid flowchart syntax directly from the plan data
- Apply appropriate styling based on resource actions (create, update, delete, etc.)
- Output in Markdown format for easy integration with documentation and PR comments
- Implementation in the Go component:

```go
func generateMermaidDiagram(plan *Plan, writer io.Writer) error {
    // Start Markdown code block with mermaid
    fmt.Fprintln(writer, "```mermaid")
    fmt.Fprintln(writer, "flowchart TD")
    
    // Style definitions
    fmt.Fprintln(writer, "    %% Style definitions")
    fmt.Fprintln(writer, "    classDef create fill:#28a745,color:#fff,stroke:#23903c,stroke-width:2px")
    fmt.Fprintln(writer, "    classDef update fill:#fd7e14,color:#fff,stroke:#d8690f,stroke-width:2px")
    fmt.Fprintln(writer, "    classDef destroy fill:#dc3545,color:#fff,stroke:#bd2130,stroke-width:2px")
    fmt.Fprintln(writer, "    classDef recreate fill:#ffc107,color:#000,stroke:#d39e00,stroke-width:2px,stroke-dasharray: 5 5")
    fmt.Fprintln(writer, "    classDef nochange fill:#6c757d,color:#fff,stroke:#5a6268,stroke-width:1px")
    fmt.Fprintln(writer, "    ")
    
    // Node definitions
    fmt.Fprintln(writer, "    %% Resources")
    for id, resource := range plan.Resources {
        safeID := makeSafeID(id)
        label := fmt.Sprintf("%s.%s", resource.Type, resource.Name)
        fmt.Fprintf(writer, "    %s[\"%s\"]\n", safeID, label)
    }
    fmt.Fprintln(writer, "    ")
    
    // Edge definitions
    fmt.Fprintln(writer, "    %% Relationships")
    for _, rel := range plan.Relationships {
        sourceID := makeSafeID(rel.Source)
        targetID := makeSafeID(rel.Target)
        fmt.Fprintf(writer, "    %s --> %s\n", sourceID, targetID)
    }
    fmt.Fprintln(writer, "    ")
    
    // Style applications
    fmt.Fprintln(writer, "    %% Apply styles based on actions")
    for id, resource := range plan.Resources {
        safeID := makeSafeID(id)
        cssClass := getCSSClassForAction(resource.Action)
        fmt.Fprintf(writer, "    %s:::%s\n", safeID, cssClass)
    }
    
    // End Markdown block
    fmt.Fprintln(writer, "```")
    
    return nil
}

// Helper functions
func makeSafeID(id string) string {
    // Convert resource ID to safe Mermaid node ID
    // Replace dots, special chars, etc.
    id = strings.Replace(id, ".", "_", -1)
    id = strings.Replace(id, "-", "_", -1)
    id = strings.Replace(id, " ", "_", -1)
    return id
}

func getCSSClassForAction(action string) string {
    switch action {
    case "create":
        return "create"
    case "update":
        return "update"
    case "delete":
        return "destroy"
    case "recreate":
        return "recreate"
    default:
        return "nochange"
    }
}
```

#### Module Representation in Mermaid

For module structures, Mermaid supports subgraphs which can be used to group resources:

```Mermaid
flowchart TD
    %% Style definitions
    classDef create fill:#28a745,color:#fff,stroke-width:2px
    classDef update fill:#fd7e14,color:#fff,stroke-width:2px
    classDef destroy fill:#dc3545,color:#fff,stroke-width:2px
    
    subgraph networking_module
        vpc["aws_vpc.main"]:::create
        subnet["aws_subnet.public_1"]:::create
        igw["aws_internet_gateway.main"]:::update
    end
    
    subgraph database_module
        db["aws_db_instance.main"]:::create
        sg["aws_security_group.db"]:::nochange
    end
    
    vpc --> subnet
    vpc --> igw
    subnet --> db
    sg --> db

```

#### Mermaid Diagram Trigger

The Mermaid diagram is automatically generated when:
- Node count exceeds configurable threshold (default: 500 nodes)
- User explicitly requests Mermaid output via `--output-format=mermaid` flag
- Rendering would exceed memory limits

#### Mermaid Diagram Benefits

- Wide support in Markdown viewers (GitHub, GitLab, Bitbucket, etc.)
- No image rendering required
- Interactive in many environments (e.g., GitHub will render the diagram)
- Easily included in documentation and PR comments
- Well-structured and maintainable format
- Visually consistent with other documentation
- Can represent both resource relationships and module hierarchy
- Can handle hundreds of nodes while remaining readable
```

