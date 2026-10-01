# Commands Overview

Bruin provides a comprehensive CLI for managing your data pipelines. Commands can be executed in multiple ways:

- **Terminal**: Direct CLI usage via `bruin <command>`
- **VS Code Extension**: Visual interface with integrated command execution
- **AI Agents**: Programmatic access via [Bruin MCP](../getting-started/bruin-mcp.md)

## Getting Help

```bash
# List all available commands
bruin --help

# Get help for a specific command
bruin run --help
bruin validate --help
```

## Command Reference

### Pipeline Execution

| Command | Description |
|---------|-------------|
| [`run`](run.md) | Execute pipelines or individual assets |
| [`backfill`](backfill.md) | Execute and resume partitioned historical ranges |
| [`validate`](validate.md) | Check pipeline configuration and syntax without executing |

### Project Management

| Command | Description |
|---------|-------------|
| [`init`](init.md) | Create a new Bruin project from a template |
| [`clean`](clean.md) | Remove temporary files and build artifacts |
| [`format`](format.md) | Format asset files for consistency |

### Connections & Environments

| Command | Description |
|---------|-------------|
| [`connections`](connections.md) | List, add, delete, and test connections |
| [`environments`](environments.md) | Manage deployment environments |

### Development & Debugging

| Command | Description |
|---------|-------------|
| [`render`](render.md) | Preview rendered Jinja templates |
| [`lineage`](lineage.md) | Visualize asset dependencies |
| [`query`](query.md) | Execute ad-hoc queries against connections |
| [`curl`](curl.md) | Call remote services with connection-aware Jinja rendering |
| [`data-diff`](data-diff.md) | Compare data between connections |

### Asset Operations

| Command | Description |
|---------|-------------|
| [`import`](import.md) | Import existing resources as Bruin assets |
| [`patch`](patch.md) | Apply patches to asset definitions |
| [`ai enhance`](ai-enhance.md) | Enhance asset metadata using AI |
| [`ai skills`](ai-skills.md) | Install or update Bruin-provided AI agent skills |

### Maintenance

| Command | Description |
|---------|-------------|
| [`upgrade`](update.md) | Upgrade Bruin CLI to the latest version or a specific version |

### Bruin Cloud

| Command | Description |
|---------|-------------|
| [`cloud`](cloud.md) | Interact with Bruin Cloud: list projects, manage pipelines, diagnose runs, and more |

## Common Workflows

### Running a Pipeline

```bash
# Run the pipeline in the current directory
bruin run

# Run a specific pipeline
bruin run ./pipelines/analytics/

# Run a specific asset
bruin run ./pipelines/analytics/assets/daily_summary.sql

# Run with a specific environment
bruin run --environment production

# Run for a specific date range
bruin run --start-date 2024-01-01 --end-date 2024-01-31
```

### Validating Before Running

```bash
# Validate pipeline syntax and configuration
bruin validate

# Validate a specific pipeline
bruin validate ./pipelines/analytics/
```

### Creating a New Project

```bash
# Initialize with the default template
bruin init default my-project

# Initialize with a specific template
bruin init chess my-chess-project
```

### Testing Connections

```bash
# List all configured connections
bruin connections list

# Test a specific connection
bruin connections test --name my-postgres-connection
```

### Debugging Templates

```bash
# Render a SQL asset to see the final query
bruin render ./assets/my_query.sql

# Render with specific date parameters
bruin render ./assets/my_query.sql --start-date 2024-01-01 --end-date 2024-01-02
```

## Global Flags

These flags are available on all commands:

| Flag | Description |
|------|-------------|
| `--debug` | Enable debug logging |
| `--help` | Show help for the command |

> [!NOTE]
> The `--environment` and `--config-file` flags are available on most commands but are per-command options, not true global flags.

## VS Code Extension

The [Bruin VS Code Extension](../vscode-extension/overview.md) provides a visual interface for many CLI commands:

- Run pipelines and assets with a single click
- View real-time execution logs
- Explore asset lineage graphically
- Preview rendered queries

## Bruin MCP (AI Agent Integration)

[Bruin MCP](../getting-started/bruin-mcp.md) enables AI agents and tools to interact with Bruin programmatically. This allows:

- Natural language pipeline execution
- Automated pipeline management
- Integration with AI-powered development workflows

## Related Topics

- [Run Command](run.md) - Detailed execution options
- [Validate Command](validate.md) - Pipeline validation
- [Cloud Command](cloud.md) - Bruin Cloud CLI
- [VS Code Extension](../vscode-extension/overview.md) - Visual interface
- [Bruin MCP](../getting-started/bruin-mcp.md) - AI agent integration
