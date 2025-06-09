# Mille Web Frontend

This is the SvelteKit-based web frontend for Mille, a Terraform/OpenTofu plan visualization tool.

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│  SvelteKit App  │───▶│   Go Backend    │───▶│  Python Render  │
│   (Frontend)    │    │   (API/CLI)     │    │   (Diagrams)    │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                       │                       │
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   Web Browser   │    │  TF Plan Parser │    │   Graphviz      │
│    (User)       │    │   (JSON/HCL)    │    │  (Rendering)    │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Interaction

1. **User uploads Terraform plan** via the SvelteKit web interface
2. **SvelteKit frontend** sends the plan to the Go backend via `/api/*` endpoints
3. **Go backend** parses the Terraform plan and extracts resource relationships
4. **Go backend** calls the Python renderer to generate visualization data
5. **Python renderer** uses the `diagrams` library and Graphviz to create infrastructure diagrams
6. **Generated visualization** is returned to the frontend and displayed using D3.js

## Project Structure

```
web/
├── src/
│   ├── routes/              # SvelteKit pages and API routes
│   │   └── +page.svelte     # Main application page
│   ├── lib/                 # Shared components and utilities
│   │   ├── Layout.svelte    # Main layout component
│   │   └── api.ts          # API client for Go backend
│   ├── components/          # Reusable UI components
│   │   └── Visualization.svelte  # D3.js-based visualization component
│   └── app.html            # Main HTML template
├── static/                  # Static assets (favicon, etc.)
├── svelte.config.js        # SvelteKit configuration
├── vite.config.js          # Vite configuration with API proxy
├── package.json            # Dependencies and scripts
└── README.md              # This file
```

## Setup Instructions

### Prerequisites

- Node.js 18+ 
- npm or yarn package manager
- Go backend running on `localhost:8080` (for API endpoints)

### Installation

1. **Navigate to the web directory:**
   ```bash
   cd web
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to `http://localhost:5173` (or the port shown in the terminal)

### Available Scripts

- `npm run dev` - Start development server with hot reload
- `npm run build` - Build the application for production
- `npm run preview` - Preview the built application
- `npm run check` - Run TypeScript and Svelte checks
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## Development Workflow

### API Integration

The SvelteKit app communicates with the Go backend through RESTful API endpoints:

- `POST /api/plans/upload` - Upload Terraform plan file
- `GET /api/plans` - List uploaded plans
- `GET /api/plans/:id` - Get specific plan details
- `GET /api/plans/:id/visualization` - Get visualization data
- `DELETE /api/plans/:id` - Delete a plan

During development, Vite proxies API requests to `http://localhost:8080` where the Go backend should be running.

### Adding New Features

1. **New Pages:** Add `.svelte` files in `src/routes/`
2. **Components:** Add reusable components in `src/components/`
3. **Utilities:** Add shared logic in `src/lib/`
4. **API Methods:** Extend the API client in `src/lib/api.ts`

### Styling

The project uses vanilla CSS with component-scoped styles. Key design principles:

- Bootstrap-inspired color scheme (`#f8f9fa`, `#495057`, etc.)
- Responsive design with mobile-first approach
- Consistent spacing and typography
- Accessible color contrasts

## Technology Stack

- **Framework:** SvelteKit 2.x
- **Language:** TypeScript
- **Visualization:** D3.js for interactive diagrams
- **Build Tool:** Vite
- **Styling:** Vanilla CSS (component-scoped)
- **Linting:** ESLint + Prettier
- **Deployment:** Static build (adapter-static)

## Production Deployment

The application builds to static files that can be served by the Go backend or any static file server:

```bash
npm run build
```

This creates a `build/` directory with all static assets that can be served directly.

## Contributing

1. Follow the existing code style (use Prettier for formatting)
2. Add TypeScript types for all new interfaces
3. Write component tests where appropriate
4. Ensure responsive design for all new components
5. Update this README for any architectural changes