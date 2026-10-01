# Core Concepts

Bruin is built around a few simple but powerful concepts. This page gives a brief orientation — each concept links to its full documentation.

| Concept | Description |
|---------|-------------|
| [Pipelines](../pipelines/definition.md) | A group of assets that are executed together in dependency order |
| [Assets](../assets/definition-schema.md) | Anything that carries value derived from data (tables, views, files, models) |
| [Semantic Layer](semantic-layer.md) | Reusable business metrics, dimensions, segments, and safe joins defined in YAML |
| [Variables](../variables/overview.md) | Dynamic values injected into your asset code during execution |
| [Connections](../connections/overview.md) | Named configurations for authenticating with data platforms and sources |
| [Commands](../commands/overview.md) | CLI operations to run, validate, and manage your pipelines |
| [Project](project.md) | A Git repository containing your pipelines, configured via `.bruin.yml` |
| Orchestration | How Bruin executes pipelines — scheduling, dependency resolution, concurrency, and deployment |

## Orchestration

Bruin orchestrates pipeline execution through several features that work together:

- **[Dependencies](../assets/definition-schema.md#depends)**: Assets declare their dependencies via the [`depends`](../assets/definition-schema.md#depends) field. Bruin uses this to determine execution order — assets run only after all their upstream dependencies have succeeded, and assets without dependencies on each other run in parallel automatically.
- **[Lineage](../commands/lineage.md)**: The dependency graph forms a lineage that lets you trace how data flows through your pipeline. You can visualize it via the [`lineage` command](../commands/lineage.md) or the [VS Code lineage panel](../vscode-extension/panels/lineage-panel.md). In Bruin Cloud, lineage extends [across pipelines](../cloud/cross-pipeline.md).
- **[Scheduling](../pipelines/definition.md#schedule)**: Pipelines can be scheduled using cron expressions in `pipeline.yml`, defining when and how often they run.
- **[Concurrency](../getting-started/concurrency.md)**: Control how many assets run simultaneously (`--workers`) and how many pipeline runs can overlap (`concurrency` setting in Bruin Cloud).
- **[Deployment](../deployment/overview.md)**: Run pipelines with Bruin Cloud, on VMs with cron, via CI/CD (GitHub Actions, GitLab), or on cloud infrastructure (AWS Lambda, ECS, Google Cloud Run).
- **[Bruin Cloud](../cloud/overview.md)**: Managed orchestration with scheduling, monitoring, notifications, and cross-pipeline dependencies — no infrastructure to manage.
