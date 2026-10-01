# AI Agents

AI agents are configurable assistants that live inside Bruin Cloud. Each agent can be scoped to a project, attached to a [connection set](../connections.md#connection-sets-for-ai-agents), connected to messaging platforms, and given a custom system prompt. The same agent can be used in chat, embedded in [Slack, Microsoft Teams, Discord, WhatsApp, or Telegram](../integrations/overview.md), scheduled to run on a cadence, or used to build dashboards.

## How agents work

When you send an agent a prompt, it:

- Spins up a sandbox environment.
- Clones the repo of the project it is connected to (if any).
- Reads your pipelines, assets, and any `AGENTS.md` or instruction files.
- Builds a memory of that context so it can answer questions in the right scope.
- Uses the agent's [connection set](../connections.md#connection-sets-for-ai-agents) to query the data warehouse, typically starting by inspecting the schema to map out available tables.

If the agent has **Cloud CLI access** enabled, it can also operate Bruin Cloud itself: read pipeline run history, inspect assets, trigger pipelines, and query the catalog and glossary.

For how the underlying data is scoped and retained, see [Does the agent see my actual data?](../faq.md#does-the-agent-see-my-actual-data) in the FAQ.

## What is in this section

- [Configure Agents](configure.md): create an agent, pick a project, attach a connection set, add messaging integrations, set permissions.
- [Chat with Agents](chat.md): use the agent in the Bruin Cloud chat for analysis, reporting, and CLI tasks.
- [Scheduled Agents](scheduled.md): run an agent on a cadence (daily reports, threshold alerts, custom SQL runs).
- [Integrations](../integrations/overview.md): connect an agent to Slack, Microsoft Teams, Discord, WhatsApp, or Telegram so your team can query data from where they already chat.
- [Slack AI Analyst tutorial](slack-ai-analyst.md): end-to-end walkthrough that builds a pipeline, enhances metadata, and deploys an analyst to Slack.

## Where agents fit

| Use case                                  | Where                                                |
| ----------------------------------------- | ---------------------------------------------------- |
| Ask one-off data questions                | **AI → Chats**                                       |
| Embed answers in your team's chat tool    | Messaging [integrations](../integrations/overview.md) (Slack, Teams, Discord, WhatsApp, Telegram) |
| Generate dashboards from prompts          | **AI → Dashboards**                                  |
| Send daily/weekly reports automatically   | **AI → [Scheduled Agents](scheduled.md)** |
| Manage pipelines from the terminal via AI | [Cloud MCP](../mcp-setup.md)                        |

## Related CLI concepts

When an agent reads your repo, it interprets it through the same primitives the CLI uses:

- [Project structure](../../core-concepts/project.md), [`AGENTS.md`](../../getting-started/glossary.md), and the [Glossary](../../getting-started/glossary.md).
- [Asset definition schema](../../assets/definition-schema.md) — how the agent knows what each asset is.
- [`bruin ai-enhance`](../../commands/ai-enhance.md) — the local-CLI equivalent of asset suggestions in the cloud.
