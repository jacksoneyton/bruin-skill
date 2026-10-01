---
name: bruin-expert
description: Use when planning, designing, writing, reviewing, or explaining anything in a Bruin project. Covers pipeline.yml, assets (SQL, Python, R, ingestr, seed, sensor, source, dashboard), materialization strategies, columns and quality checks, variables, connections and platforms such as Snowflake, .bruin.yml environments and secret providers, CLI commands, templates, CI/CD and deployment, Bruin Cloud, and the VS Code extension. Read this before planning or generating any Bruin pipeline or asset, and before stating Bruin syntax from memory.
---

# Bruin Expert

This skill makes the agent reliable at designing Bruin pipelines and assets. It carries the full Bruin documentation as local reference files, plus complete example pipelines from the Bruin templates. It complements the bundled Bruin skills in this folder (`pipeline-diagnose`, `schema-drift-check`, `duplicate-investigate`, `freshness-check`, `quality-check-investigate`, `maintenance-action`, `bruin-semantic-layer`). Those handle diagnosis and semantic layers. This skill handles authoring and planning.

## Rules for using it

1. Do not write Bruin syntax from memory. Asset fields, materialization options, check names, and CLI flags change between releases. Open the reference page first, then write.
2. Load references progressively. Open `references/INDEX.md`, then the one category index you need, then only the pages that index points to. Do not read whole categories.
3. Before writing a new asset, find a similar working example in `references/template-sources/` (see `references/_indexes/template-sources.md`) and follow its layout.
4. If the installed CLI behaves differently from a reference page, trust `bruin <command> --help`, tell the user about the discrepancy, and continue with the CLI's behavior. `references/SOURCE.md` records which upstream commit the references came from.
5. Follow the guardrails in the section below on environments and destructive operations.

## Where to look

All paths are relative to this skill folder. Each index lists every page in the category with a one-line summary.

| Task | Index | Read these pages first |
|---|---|---|
| Understand the model, first project | `references/_indexes/core-concepts.md` | `core-concepts/project.md`, `core-concepts/overview.md`, `getting-started/design-principles.md` |
| Pipeline layout, schedule, defaults, variants | `references/_indexes/pipelines.md` | `pipelines/definition.md` |
| Asset definition, SQL, Python, R, seed, sensor, dashboard | `references/_indexes/assets.md` | `assets/definition-schema.md`, then the asset type page |
| Materialization strategies, incremental loads, SCD2 | `references/_indexes/assets.md` | `assets/materialization.md`, `assets/interval-modifiers.md` |
| Columns, descriptions, column-level checks | `references/_indexes/assets.md` | `assets/columns.md`, `quality/available_checks.md` |
| Jinja, macros, filters | `references/_indexes/assets.md` | `assets/templating/templating.md` |
| Variables (built-in, custom, `--var`) | `references/_indexes/variables.md` | `variables/overview.md` |
| Connection config, platform specifics (Snowflake and others) | `references/_indexes/connections-platforms.md` | `connections/overview.md`, `platforms/<platform>.md` |
| Copying data from SaaS, databases, files (ingestr) | `references/_indexes/data-ingestion.md` | `assets/ingestr.md`, `ingestion/overview.md`, `ingestion/<source>.md` |
| CLI usage and flags | `references/_indexes/commands.md` | `commands/<command>.md` |
| Quality checks, custom checks, unit tests, policies | `references/_indexes/data-governance.md` | `quality/overview.md`, `quality/custom.md`, `quality/unit-tests.md`, `getting-started/policies.md` |
| Deployment, schedulers, CI/CD | `references/_indexes/deployment-cicd.md` | `deployment/overview.md`, then the target page |
| `.bruin.yml`, secret backends | `references/_indexes/secret-providers.md` | `secrets/overview.md`, `secrets/bruinyml.md` |
| Starter pipelines, migration templates | `references/_indexes/templates.md` and `references/_indexes/template-sources.md` | `getting-started/templates.md` |
| VS Code extension, Bruin MCP, dev environments | `references/_indexes/developer-tools.md` | `getting-started/bruin-mcp.md`, `getting-started/devenv.md` |
| Bruin Cloud (orchestration, catalog, agents, governance) | `references/_indexes/bruin-cloud.md` | `cloud/overview.md` |

## Core model

- A project is a Git repository. `.bruin.yml` at the repo root holds environments, connections, and secrets. Bruin creates it on first use and adds it to `.gitignore`. Credentials can come from `${ENV_VAR}` references or a secret backend (Vault, Doppler, AWS Secrets Manager). Never commit real credentials.
- A pipeline is a folder with a `pipeline.yml` and an `assets/` folder next to it. `pipeline.yml` sets name, schedule, `start_date`, `default_connections`, `default` (values applied to every asset), `variables`, retries, and similar. See `references/pipelines/definition.md`.
- An asset is one unit of work, defined in a single file:
  - `.sql`: definition in a `/* @bruin ... @bruin */` block at the top of the same file as the query.
  - `.py`: definition in a `"""@bruin ... @bruin"""` block at the top of the same file as the code.
  - `<name>.asset.yml` or `.asset.yaml`: standalone YAML for assets with no code body (ingestr, seed, sensor, dashboard, source). Plain `.yml` files are ignored.
  - A SQL asset's definition and query cannot be split across two files. Bruin treats a sibling `.asset.yml` as an unrelated asset.
- `type` selects the platform and kind, for example `sf.sql`, `sf.seed`, `sf.source`, `sf.sensor.table`, `sf.sensor.query` for Snowflake, `bq.sql` for BigQuery, `ingestr`, `python`. The exact type names per platform are on the platform page.
- Execution order comes from `depends`. Items are asset names in the same pipeline, or objects with `asset`, `uri`, and `mode` (`full` or `symbolic`, where symbolic only draws lineage).
- `materialization` controls how a query result is persisted: `type` (`table` or `view`) and `strategy`. Strategies documented in `references/assets/materialization.md`: `create+replace`, `delete+insert`, `truncate+insert`, `append`, `merge`, `time_interval`, `DDL`, Data Vault strategies, `scd2_by_column`, `scd2_by_time`. Required companion fields (`incremental_key`, primary keys on columns, `partition_by`, `cluster_by`) differ by strategy and platform, so read that page before choosing.
- `columns` declares name, type, description, and `checks` (built-in checks listed in `references/quality/available_checks.md`). `custom_checks` holds SQL checks. Checks run after the asset and a failing blocking check stops downstream assets.
- Pipeline `default` values fill empty asset fields. Scalars fill only if unset, maps merge without overwriting, lists add missing entries.
- Environments: `default_environment` plus an `environments` map in `.bruin.yml`. `schema_prefix` per environment prefixes schema names, so `mart.customers` becomes `jane_mart.customers`.

## Planning workflow for a new pipeline or asset

Do these in order and write down the decisions before writing files.

1. Clarify scope with the user: source, destination platform and connection, grain (what one row is), freshness and schedule, full versus incremental, which environment to develop in, who owns it.
2. Inspect the project: nearest `pipeline.yml`, existing assets and naming, `bruin connections list`, existing checks, and a baseline `bruin validate <pipeline>`.
3. Pick the asset type for each step:
   - Copy from a source system into the warehouse: `ingestr` asset. Check `references/ingestion/<source>.md` for the source's connection fields and tables.
   - Transform inside the warehouse: SQL asset with the platform's `*.sql` type.
   - API calls, custom logic, dataframes: Python asset.
   - Static reference data: `seed`. Waiting on an external table or query: `sensor`.
   - Document a table Bruin does not build, for lineage and descriptions: `*.source` asset (for Snowflake, `sf.source`).
4. Pick materialization from the grain and load pattern. Full rebuild: `create+replace`. Append-only facts: `append`. Upsert by key: `merge`. Reload a slice: `delete+insert` or `time_interval`. History tracking: `scd2_*`. Confirm requirements in `references/assets/materialization.md`, then check the platform page for platform-specific options.
5. Define columns, types, descriptions, and checks. Query the real data first to confirm grain, nullability, and uniqueness before encoding checks. Choose `blocking` deliberately. The docs disagree on the default for custom checks (`quality/overview.md` and `quality/custom.md` say `blocking` defaults to true, the custom checks table in `assets/definition-schema.md` lists false), so set `blocking` explicitly.
6. Wire `depends`, then confirm lineage with `bruin lineage`.
7. Parameterize with pipeline `variables` rather than hardcoding values. Each variable needs a `default`.
8. Verify in this order: `bruin validate`, `bruin render` to inspect rendered SQL, a limited run in a non-production environment, then checks.
9. Write a `README.md` in the pipeline folder: purpose, source tables, dependencies, environment assumptions, how to run and troubleshoot.

## Command quick reference

Confirm flags in `references/commands/<command>.md` before using anything unfamiliar.

| Need | Command |
|---|---|
| Check config and syntax | `bruin validate <path>` (`--fast` skips query validation) |
| See rendered SQL | `bruin render <asset>` |
| Run a pipeline or asset | `bruin run <path> --environment <env>` |
| Run subsets | `--tag`, `--exclude-tag`, `--selector`, `--downstream`, `--only checks`, `--continue` |
| Date window | `--start-date`, `--end-date` (both default to yesterday on the CLI) |
| Override variables | `--var '{"name":"value"}'` |
| Rebuild from scratch | `--full-refresh` (destructive, see guardrails) |
| Historical ranges | `bruin backfill <pipeline> --start-date ... --end-date ... --partition daily` (supports `--dry-run`) |
| Ad hoc queries | `bruin query --connection <name> --query "..." --limit 20`, or `--asset <path>` |
| List and test connections | `bruin connections list`, `bruin connections test --name <connection> [--env <env>]` |
| Lineage | `bruin lineage <asset>` |
| Import existing tables as assets | `bruin import database ...` |
| Draft table and column descriptions | `bruin ai enhance` (review the output, do not treat it as authoritative) |
| Install the bundled agent skills | `bruin ai skills all` |
| Compare data across connections | `bruin data-diff` |

Interval modifiers are applied automatically in Bruin Cloud and only with `--apply-interval-modifiers` on the CLI. `concurrency` and `max_active_steps` apply to Bruin Cloud, not to local `bruin run`.

## Snowflake notes

Full detail is in `references/platforms/snowflake.md`.

- Connection fields: `name`, `username`, `account`, `database`, `region` (documented as required), optional `schema`, `warehouse`, `role`. Authenticate with `password`, or key pair via `private_key_path` or `private_key` (set `password` to the passphrase for an encrypted key).
- `read_only: true` on a connection rejects writes at the Bruin layer. It is not a substitute for a restricted Snowflake role.
- Asset names can be `table`, `schema.table`, or `database.schema.table`. A three-part name makes Bruin run `CREATE DATABASE IF NOT EXISTS`, so the role needs that privilege.
- A per-asset `warehouse` parameter overrides the connection default. It accepts Jinja, so `parameters: warehouse: "{{ var.warehouse }}"` with a pipeline variable allows a one-off larger-warehouse rerun via `--var`.
- `--query-annotations` sets `QUERY_TAG` with asset and pipeline for tracing in `QUERY_HISTORY`.

## Guardrails

These match the upstream `AGENTS.md` guidance that `bruin ai skills all` installs.

- Run in the `dev` or default non-production environment unless the user explicitly asks for production. State the environment in every response that runs commands.
- Get explicit confirmation before `--full-refresh`, backfills, or anything that replaces data, unless the user gave specific instructions.
- Keep queries narrow: select needed columns, add limits, filter partitions and date ranges. Do not query sensitive columns unless the task needs them.
- Keep changes scoped to the affected pipeline, asset, checks, or docs. Validate after meaningful changes, not after every small edit.
- If validation or a run cannot be executed, say why and give the exact command for the user to run.
- Report commands run, environment used, files changed, and results.

## Keeping the references current

The references are generated from `docs/` and `templates/` in `bruin-data/bruin`. Regenerate with `tools/sync.sh` from the root of the repository this skill ships in. The script needs git and Python 3 only and does a sparse checkout of the two folders. After a refresh, check `references/SOURCE.md` for the commit.
