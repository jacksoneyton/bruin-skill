# Getting Started

Bruin Cloud has two tracks. Pick the one that matches what you want to do first — you can set up the other later from the same workspace.

<div class="track-grid">
  <a href="#ai-data-analyst-track" class="track-card">
    <div class="track-badge ai">AI</div>
    <h3>AI Data Analyst</h3>
    <p>Connect a warehouse, ask questions in plain English, get charts and reports back. Push answers into Slack, Teams, or WhatsApp.</p>
    <ul>
      <li>Best for analysts and PMs</li>
      <li>Connect once, ask anything</li>
      <li>No code required</li>
    </ul>
    <span class="track-cta">Start with AI Data Analyst →</span>
  </a>
  <a href="#etl-elt-pipeline-track" class="track-card">
    <div class="track-badge etl">ETL</div>
    <h3>ETL/ELT Pipeline</h3>
    <p>Define SQL and Python transforms in Git, then schedule them. Bruin parses, validates, and runs your pipelines automatically.</p>
    <ul>
      <li>Best for data engineers</li>
      <li>Git-based, code-first workflow</li>
      <li>Scheduled SQL + Python transforms</li>
    </ul>
    <span class="track-cta">Start with ETL/ELT Pipeline →</span>
  </a>
</div>

## Before you start

**Sign up** at [cloud.getbruin.com/register](https://cloud.getbruin.com/register) with email and password, or sign in with Google. Right after sign-up, Bruin Cloud asks which track you want — pick **AI Data Analyst** or **ETL/ELT Pipeline**.

If you'd rather start in code, the open-source [Bruin CLI](../getting-started/introduction/installation.md) defines the same pipelines, assets, and connections Bruin Cloud runs. Start with the [Quickstart](../getting-started/introduction/quickstart.md), then connect your repo to Cloud.

> [!TIP]
> You can switch tracks at any time from **Getting Started** on the home page. The toggle is labelled **AI Analyst** / **Data Engineer**.

## AI Data Analyst track

Connect a warehouse, ask the agent questions, then push answers into your team's chat tools.

**1. Connect your data.** Add a [connection](connections.md) to a warehouse the agent should read from — BigQuery, Postgres, MySQL, SQL Server, Snowflake, Databricks, or Redshift. Create with validation so Bruin can confirm the credentials work.

> [!TIP]
> No warehouse credentials yourself? Invite a teammate from your data team and have them set the connection up. The agent then becomes available to the whole workspace.

**2. Ask your first question.** Open **AI → Chats**, pick the default agent, and try:
> What data do you have access to?

The agent inspects the schema and tells you what's available. From there, ask the questions that matter — revenue, retention, top SKUs, whatever your team needs. See [Chat with Agents](ai-agents/chat.md).

**3. Connect a chat platform.** Open **AI → Agents**, pick the agent, and wire it to where your team already works:

- [Slack](integrations/slack.md) — OAuth install, then a Channel ID per agent
- [Microsoft Teams](integrations/teams.md) — `connect BRN-XXXX` in a channel, group chat, or 1:1
- [Google Chat](integrations/google-chat.md) — `connect BRN-XXXX` in a DM or space
- [Discord](integrations/discord.md) — bot install, then `/bruin` in any wired channel
- [WhatsApp](integrations/whatsapp.md) — message Bruin's number with `connect BRN-XXXX`
- [Telegram](integrations/telegram.md) — DM [@BruinDataBot](https://t.me/BruinDataBot) with `connect BRN-XXXX`

**4. Build a dashboard.** Open **AI → Dashboards** and describe what you want. The agent assembles charts, tables, and metrics from your prompt; iterate until it looks right, then click **Publish**. See [Dashboards](dashboards.md).

**5. Schedule a report.** Have the agent run on a cadence and post results into your chat tool. Daily revenue summaries, weekly retention alerts, threshold-based notifications. See [Scheduled Agents](ai-agents/scheduled.md).

**6. (Optional) Add a context layer.** Connect a Git repo with your dbt or Bruin semantic layer so the agent learns your team's vocabulary and metric definitions. Or describe tables manually for the metrics that matter most. Both options are in [Team Settings → Projects](team-settings.md#projects).

## ETL/ELT Pipeline track

Wire a Git repo, configure the connections your pipelines need, enable them, then monitor.

**1. Create a project.** A [project](../core-concepts/project.md) in Bruin Cloud maps one-to-one with a Git repository. Creating one syncs the pipelines in that repo and gives you a place to manage their connections.

> [!TIP]
> Use the **Bruin GitHub App** instead of a personal access token where possible — fine-grained access, no expiring tokens, repo-level installs. See [Projects](projects.md#github-authentication).

**2. Add connections.** While the project syncs, open **Connections** and add the data sources, destinations, and secrets your pipelines reference. These are the same connections you'd define locally in `.bruin.yml`, but encrypted in Bruin Cloud's [HashiCorp Vault](../secrets/vault.md) instead of your repo.

See [Connections](connections.md) for connection types, naming rules, and the validation flow.

**3. Enable a pipeline.** Pipelines synced from a repo start disabled. Open **Catalog → Pipelines**, pick one, and click **Enable selected pipelines**. If any referenced connections are missing, Bruin Cloud lists them and lets you add each one inline.

> [!INFO]
> The first run triggers automatically when you enable a new pipeline. You don't need to click **New run** yourself.

**4. Monitor and operate.** Once a pipeline is active, the pipeline page is your operations console:

- **Runs panel** for status and history. See [Runs](runs.md).
- **Assets** for every asset with its type, owner, schedule, last run. See [Assets](assets.md).
- **Backfills** for historical reprocessing. See [Backfills](backfills.md).
- **Lineage** for how assets connect. See [Catalog → Lineage](catalog.md#global-lineage).
- **New run** for ad-hoc runs, full refreshes, and backfills.

**5. Set up notifications.** Create rules under **Team Settings → Notifications**, or use legacy notification settings in `pipeline.yml`. See [Notifications](notifications.md).

**6. (Optional) Cross-pipeline dependencies.** If pipelines in different repos depend on each other's assets, wire them up with URIs instead of duplicating definitions. See [Cross-pipeline dependencies](cross-pipeline.md).

## After the first run

These apply regardless of which track you started with:

- [Team Settings](team-settings.md) — members, projects, billing, audit logs
- [API Tokens](api-tokens.md) — programmatic access (CI, MCP, external monitoring)
- [Insights](insights.md) — cost explorer, pipeline health, risk report, usage
- [Cloud MCP](mcp-setup.md) — talk to Bruin Cloud from Cursor, Claude Code, or Codex
- [FAQ](faq.md) — common questions and patterns that aren't real features
