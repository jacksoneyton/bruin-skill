# Bruin Cloud

[Bruin Cloud](https://cloud.getbruin.com/register) is a managed platform built on top of the open-source [Bruin CLI](../getting-started/introduction/installation.md). It runs your pipelines on a schedule, stores your connections securely, gives you a UI for monitoring runs and lineage, and ships an AI layer that can chat with your data, build dashboards, and answer questions in tools like Slack and Teams.

> [!INFO]
> This section of the documentation covers Bruin Cloud. If you are looking for the open-source CLI, start at the [Quickstart](../getting-started/introduction/quickstart.md).

## What you get

- Managed scheduling: pipelines defined in your Git repo run on their configured schedule without you running a server.
- Connections and secrets: BigQuery, Snowflake, Postgres, Databricks, S3, and dozens of other platforms configured through the UI. Credentials are encrypted at rest with [HashiCorp Vault](../secrets/vault.md).
- Run monitoring: [runs](runs.md), logs, [lineage](catalog.md#global-lineage), [backfills](backfills.md), manual runs, and per-asset history for every pipeline.
- AI agents and [dashboards](dashboards.md): configurable agents scoped to projects and [connection sets](connections.md#connection-sets-for-ai-agents). Use them in the Bruin Cloud chat, embed them in [Slack, Teams, Google Chat, Discord, WhatsApp, or Telegram](integrations/overview.md), schedule them, or build dashboards with them.
- Cross-pipeline dependencies: depend on assets that live in a different pipeline or repo using URIs.
- [Insights](insights.md): cost explorer, pipeline health, risk report, and usage tracking.
- [Catalog](catalog.md) and [governance](governance.md): a glossary, owners, and built-in quality rules that score every asset.
- Team administration: [team settings](team-settings.md), [API tokens](api-tokens.md), and a full [audit log](audit-logs.md).

## How to read these docs

If you are new to Bruin Cloud, start with [Getting Started](getting-started.md). It walks through wiring up a Git repo, adding connections, and enabling your first pipeline.

If you haven't installed the open-source CLI yet, the cloud docs assume you'll be defining pipelines in code — [Quickstart](../getting-started/introduction/quickstart.md), [Pipeline definition](../pipelines/definition.md), and [Asset definition schema](../assets/definition-schema.md) are the starting points there.

From there:

- [Projects](projects.md): connect a Git repo, choose between the GitHub App and a personal access token, migrate existing projects.
- [Connections](connections.md): configure the connections your pipelines and agents use.
- [Pipelines](pipelines.md): enable pipelines, trigger runs, manage backfills, view lineage.
- [Runs](runs.md): cross-pipeline run history, rerun, mark success/failure, drill into per-asset logs.
- [Backfills](backfills.md): multi-interval re-processing across historical date ranges.
- [Assets](assets.md): asset catalog, per-asset detail, profile, columns, custom checks, AI suggestions.
- [Catalog](catalog.md): glossary, owners, and global lineage across pipelines.
- [Insights](insights.md): cost explorer, pipeline health, risk report, usage.
- [Dashboards](dashboards.md): AI-built dashboards your team can re-open without re-asking.
- [AI Agents](ai-agents/overview.md): create agents, chat with them, schedule them, deploy them to chat platforms.
- [Integrations](integrations/overview.md): connect agents to Slack, Microsoft Teams, Google Chat, Discord, WhatsApp, or Telegram.
- [Notifications](notifications.md): configurable rules for pipeline, asset, and check events, plus legacy `pipeline.yml` notifications.
- [Cross-pipeline dependencies](cross-pipeline.md): depend on assets that live in other pipelines.
- [Governance](governance.md): the rules that drive quality scores and the risk report.
- [Instance Types](instance-types.md): sizing assets at run time.
- [Security](security.md): network access and dedicated egress IPs for allowlisting.
- [Team Settings](team-settings.md), [API Tokens](api-tokens.md), [Audit Logs](audit-logs.md): team administration.
- [`cloud` command](../commands/cloud.md): list projects, check runs, diagnose failures, and drive Bruin Cloud from your terminal.
- [Cloud MCP](mcp-setup.md): talk to Bruin Cloud from Cursor, Claude Code, or Codex.
- [FAQ](faq.md): short answers to common questions, including patterns that look plausible but are not real features.

---

[Sign up for Bruin Cloud →](https://cloud.getbruin.com/register)
