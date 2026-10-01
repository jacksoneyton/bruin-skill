# Index: Commands (CLI reference)

22 pages. Paths are relative to references/.

- `commands/ai-enhance.md` | `ai enhance` Command: The ai enhance command uses AI to automatically enhance your asset definitions with meaningful metadata, quality checks, descriptions, and tags. It analyzes your asset...
- `commands/ai-skills.md` | AI Skills Command: The bruin ai skills command installs or updates Bruin-provided agent skills for a repository.
- `commands/backfill.md` | Backfill: bruin backfill splits a historical range into partitions, runs each partition through bruin run, and saves enough state to resume failed or interrupted work locally.
- `commands/clean.md` | `clean`  Command: The clean command is used to remove temporary artifacts related to Bruin.
- `commands/cloud.md` | `cloud` Command: Run Bruin Cloud commands from your terminal:
- `commands/connections.md` | Connections: Bruin has various commands to handle connections via its CLI.
- `commands/curl.md` | Curl Command: The curl command runs the installed curl executable with arguments rendered from Bruin connections. It is a pass-through wrapper, so it supports the complete option an...
- `commands/data-diff.md` | `data-diff` Command: The data-diff command compares data between two tables from the same or different data sources. By default, it performs a fast schema-only comparison. Use the --full f...
- `commands/environments.md` | `environments` Command: The environments command allows you to manage environments defined in the .bruin.yml configuration file.
- `commands/format.md` | `format` Command: The format command is used to process and format asset definition files in a project. It can handle a single asset file or process all asset files in a given path.
- `commands/import.md` | `import` Command: The import commands allow you to automatically import existing resources as Bruin assets. This includes database tables, BigQuery scheduled queries, ODI XML exports, T...
- `commands/init.md` | Init Command: The bruin init command bootstraps a new Bruin pipeline from a predefined template. It automatically sets up the folder structure, initializes configuration files, and...
- `commands/lineage.md` | `lineage` Command: The lineage command helps you understand how a specific asset fits into your pipeline by showing its dependencies. It tells you:
- `commands/login.md` | `cloud login` Command: Sign in to Bruin Cloud:
- `commands/overview.md` | Commands Overview: Bruin provides a comprehensive CLI for managing your data pipelines. Commands can be executed in multiple ways:
- `commands/patch.md` | Patch Command: The patch command provides utilities for updating asset metadata and dependencies. It has two subcommands: fill-asset-dependencies and fill-columns-from-db.
- `commands/query.md` | Query Command: The query command executes and retrieves the results of a query on a specified connection and returns the results in table format, JSON, or CSV.
- `commands/render.md` | `render` Command: The render command processes a Bruin SQL asset and generates a SQL query or materialized output for execution.
- `commands/run.md` | `run` Command: To split a historical range into resumable partitions, use bruin backfill.
- `commands/unit-test.md` | `unit-test` Command: bruin unit-test runs an asset's unit tests against its configured connection. Each test mocks the tables the query reads, runs one read-only SELECT, and compares the o...
- `commands/update.md` | Upgrade Command: The bruin upgrade command updates your Bruin CLI installation to the latest version directly from the command line.
- `commands/validate.md` | `validate` Command: The validate command checks the Bruin pipeline configurations for all pipelines in a specified directory or validates a single asset.
