# Index: template sources (complete example pipelines)

Real asset and pipeline files from the Bruin templates. Use them as pattern references when writing pipeline.yml, asset definitions, materialization, checks and .bruin.yml. Paths are relative to references/template-sources/.

## academy-sql-advanced

- `template-sources/academy-sql-advanced/.bruin.yml`
- `template-sources/academy-sql-advanced/AGENTS.md`
- `template-sources/academy-sql-advanced/course/README.md`
- `template-sources/academy-sql-advanced/course/answer-key.md`
- `template-sources/academy-sql-advanced/course/lessons/01-query-to-pipeline.md`
- `template-sources/academy-sql-advanced/course/lessons/02-ddl-dml-and-approval.md`
- `template-sources/academy-sql-advanced/course/lessons/03-dependencies-and-the-graph.md`
- `template-sources/academy-sql-advanced/course/lessons/04-checks-as-automated-audit.md`
- `template-sources/academy-sql-advanced/course/lessons/05-unit-test-the-logic.md`
- `template-sources/academy-sql-advanced/course/lessons/06-break-it-on-purpose.md`
- `template-sources/academy-sql-advanced/course/lessons/07-incremental-strategies.md`
- `template-sources/academy-sql-advanced/course/lessons/08-late-data-and-backfills.md`
- `template-sources/academy-sql-advanced/course/lessons/09-sargability-and-cost.md`
- `template-sources/academy-sql-advanced/course/lessons/10-dev-environments.md`
- `template-sources/academy-sql-advanced/course/lessons/11-guardrails.md`
- `template-sources/academy-sql-advanced/course/lessons/12-investigate-a-failure.md`
- `template-sources/academy-sql-advanced/course/lessons/13-logs-history-and-the-bill.md`
- `template-sources/academy-sql-advanced/course/lessons/14-capstone-ship-it.md`
- `template-sources/academy-sql-advanced/course/lessons/15-recap-and-next-steps.md`
- `template-sources/academy-sql-advanced/course/progress.md`
- `template-sources/academy-sql-advanced/docs/_data-design.md`
- `template-sources/academy-sql-advanced/docs/_implementation-notes.md`
- `template-sources/academy-sql-advanced/docs/_known-defects.md`
- `template-sources/academy-sql-advanced/docs/contracts/churn_risk.md`
- `template-sources/academy-sql-advanced/docs/contracts/weekly_category.md`
- `template-sources/academy-sql-advanced/docs/glossary.md`
- `template-sources/academy-sql-advanced/docs/runbook.md`
- `template-sources/academy-sql-advanced/docs/schema.md`
- `template-sources/academy-sql-advanced/pipeline/assets/core/dim_customer.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/core/dim_customer_history.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/core/fct_order_lines.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/customer_snapshots.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/customers.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/dates.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/fx_rates.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/order_items.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/orders.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/products.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/generate/stores.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/mart/churn_risk.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/mart/weekly_category_revenue.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/staging/stg_customers.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/staging/stg_order_items.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/staging/stg_orders.sql`
- `template-sources/academy-sql-advanced/pipeline/assets/staging/stg_products.sql`
- `template-sources/academy-sql-advanced/pipeline/pipeline.yml`
- `template-sources/academy-sql-advanced/queries/ops/late-arrival-audit.sql`
- `template-sources/academy-sql-advanced/queries/ops/sargability-functional.sql`
- `template-sources/academy-sql-advanced/queries/ops/sargability-range.sql`
- `template-sources/academy-sql-advanced/queries/ops/select-star-all.sql`
- `template-sources/academy-sql-advanced/queries/ops/select-star-columns.sql`
- `template-sources/academy-sql-advanced/queries/ops/timezone-dst-audit.sql`
- `template-sources/academy-sql-advanced/queries/reconciliation/monthly-totals.sql`
- `template-sources/academy-sql-advanced/queries/reconciliation/source-vs-mart.sql`

## academy-sql-beginner

- `template-sources/academy-sql-beginner/.bruin.yml`
- `template-sources/academy-sql-beginner/AGENTS.md`
- `template-sources/academy-sql-beginner/course/README.md`
- `template-sources/academy-sql-beginner/course/answer-key.md`
- `template-sources/academy-sql-beginner/course/lessons/01-start-here.md`
- `template-sources/academy-sql-beginner/course/lessons/02-what-to-delegate.md`
- `template-sources/academy-sql-beginner/course/lessons/03-setup.md`
- `template-sources/academy-sql-beginner/course/lessons/04-meet-the-warehouse.md`
- `template-sources/academy-sql-beginner/course/lessons/05-ask-one-table.md`
- `template-sources/academy-sql-beginner/course/lessons/06-count-sum-group.md`
- `template-sources/academy-sql-beginner/course/lessons/07-join-without-breaking.md`
- `template-sources/academy-sql-beginner/course/lessons/08-name-your-steps.md`
- `template-sources/academy-sql-beginner/course/lessons/09-ask-the-agent.md`
- `template-sources/academy-sql-beginner/course/lessons/10-audit-what-it-wrote.md`
- `template-sources/academy-sql-beginner/course/lessons/11-interrogate-the-logic.md`
- `template-sources/academy-sql-beginner/course/lessons/12-fix-the-context.md`
- `template-sources/academy-sql-beginner/course/lessons/13-save-a-query-as-an-asset.md`
- `template-sources/academy-sql-beginner/course/lessons/14-capstone-audit-lab.md`
- `template-sources/academy-sql-beginner/course/lessons/15-recap-and-next-steps.md`
- `template-sources/academy-sql-beginner/course/progress.md`
- `template-sources/academy-sql-beginner/docs/data-design.md`
- `template-sources/academy-sql-beginner/docs/failure-modes.md`
- `template-sources/academy-sql-beginner/docs/known-defects.md`
- `template-sources/academy-sql-beginner/docs/schema.md`
- `template-sources/academy-sql-beginner/docs/writing-an-asset.md`
- `template-sources/academy-sql-beginner/pipeline/assets/customers.sql`
- `template-sources/academy-sql-beginner/pipeline/assets/dates.sql`
- `template-sources/academy-sql-beginner/pipeline/assets/order_items.sql`
- `template-sources/academy-sql-beginner/pipeline/assets/orders.sql`
- `template-sources/academy-sql-beginner/pipeline/assets/products.sql`
- `template-sources/academy-sql-beginner/pipeline/assets/stores.sql`
- `template-sources/academy-sql-beginner/pipeline/pipeline.yml`
- `template-sources/academy-sql-beginner/queries/01-first-look.sql`
- `template-sources/academy-sql-beginner/queries/02-aggregates.sql`
- `template-sources/academy-sql-beginner/queries/03-joins.sql`
- `template-sources/academy-sql-beginner/queries/04-cte.sql`
- `template-sources/academy-sql-beginner/queries/anchors.md`
- `template-sources/academy-sql-beginner/queries/audit-lab/README.md`
- `template-sources/academy-sql-beginner/queries/audit-lab/_answer-key.md`
- `template-sources/academy-sql-beginner/queries/audit-lab/findings-template.md`
- `template-sources/academy-sql-beginner/queries/audit-lab/q01.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q02.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q03.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q04.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q05.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q06.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q07.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q08.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q09.sql`
- `template-sources/academy-sql-beginner/queries/audit-lab/q10.sql`
- `template-sources/academy-sql-beginner/queries/audit-template.md`

## academy-sql-intermediate

- `template-sources/academy-sql-intermediate/.bruin.yml`
- `template-sources/academy-sql-intermediate/AGENTS.md`
- `template-sources/academy-sql-intermediate/course/README.md`
- `template-sources/academy-sql-intermediate/course/answer-key.md`
- `template-sources/academy-sql-intermediate/course/lessons/01-the-question-is-the-hard-part.md`
- `template-sources/academy-sql-intermediate/course/lessons/02-write-the-model-contract.md`
- `template-sources/academy-sql-intermediate/course/lessons/03-profile-before-you-model.md`
- `template-sources/academy-sql-intermediate/course/lessons/04-stage-the-work.md`
- `template-sources/academy-sql-intermediate/course/lessons/05-window-functions.md`
- `template-sources/academy-sql-intermediate/course/lessons/06-patterns-agents-get-wrong.md`
- `template-sources/academy-sql-intermediate/course/lessons/07-read-a-query-fast.md`
- `template-sources/academy-sql-intermediate/course/lessons/08-layer-the-project.md`
- `template-sources/academy-sql-intermediate/course/lessons/09-views-and-tables.md`
- `template-sources/academy-sql-intermediate/course/lessons/10-metric-in-the-asset.md`
- `template-sources/academy-sql-intermediate/course/lessons/11-descriptions-and-tags.md`
- `template-sources/academy-sql-intermediate/course/lessons/12-glossary-and-readme.md`
- `template-sources/academy-sql-intermediate/course/lessons/13-measure-your-context.md`
- `template-sources/academy-sql-intermediate/course/lessons/14-capstone-defend-the-answer.md`
- `template-sources/academy-sql-intermediate/course/lessons/15-recap-and-next-steps.md`
- `template-sources/academy-sql-intermediate/course/progress.md`
- `template-sources/academy-sql-intermediate/docs/_data-design.md`
- `template-sources/academy-sql-intermediate/docs/contracts/TEMPLATE.md`
- `template-sources/academy-sql-intermediate/docs/eval/answers.md`
- `template-sources/academy-sql-intermediate/docs/eval/questions.md`
- `template-sources/academy-sql-intermediate/docs/glossary.md`
- `template-sources/academy-sql-intermediate/docs/schema.md`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/customers.sql`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/dates.sql`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/fx_rates.sql`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/order_items.sql`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/orders.sql`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/products.sql`
- `template-sources/academy-sql-intermediate/pipeline/assets/generate/stores.sql`
- `template-sources/academy-sql-intermediate/pipeline/pipeline.yml`
- `template-sources/academy-sql-intermediate/queries/profiling/01-row-counts.sql`
- `template-sources/academy-sql-intermediate/queries/profiling/02-key-uniqueness.sql`
- `template-sources/academy-sql-intermediate/queries/profiling/03-null-rates.sql`
- `template-sources/academy-sql-intermediate/queries/profiling/04-orphan-keys.sql`
- `template-sources/academy-sql-intermediate/queries/profiling/05-date-coverage.sql`
- `template-sources/academy-sql-intermediate/queries/profiling/06-categorical-values.sql`
- `template-sources/academy-sql-intermediate/queries/reading-drill/README.md`
- `template-sources/academy-sql-intermediate/queries/reading-drill/drill-1.sql`
- `template-sources/academy-sql-intermediate/queries/reading-drill/drill-2.sql`
- `template-sources/academy-sql-intermediate/queries/reading-drill/drill-3.sql`

## ai-coding-usage
This Bruin template ingests AI coding usage from the Anthropic and Cursor Admin APIs into DuckDB, normalizes both platforms to a shared user/day model, and builds orga...
Docs: `getting-started/templates-docs/ai-coding-usage-README.md`

- `template-sources/ai-coding-usage/.bruin.yml`
- `template-sources/ai-coding-usage/assets/marts/ai_coding_daily_summary.sql`
- `template-sources/ai-coding-usage/assets/marts/ai_coding_usage_by_user_day.sql`
- `template-sources/ai-coding-usage/assets/marts/ai_coding_usage_by_user_model_day.sql`
- `template-sources/ai-coding-usage/assets/marts/ai_coding_user_daily_summary.sql`
- `template-sources/ai-coding-usage/assets/marts/ai_coding_user_summary.sql`
- `template-sources/ai-coding-usage/assets/marts/anthropic_usage_by_user_day.sql`
- `template-sources/ai-coding-usage/assets/marts/cursor_usage_by_user_day.sql`
- `template-sources/ai-coding-usage/assets/raw/claude_code_usage.asset.yml`
- `template-sources/ai-coding-usage/assets/raw/cursor_daily_usage.asset.yml`
- `template-sources/ai-coding-usage/assets/raw/cursor_usage_events.asset.yml`
- `template-sources/ai-coding-usage/assets/staging/claude_code_usage.sql`
- `template-sources/ai-coding-usage/assets/staging/cursor_daily_usage.sql`
- `template-sources/ai-coding-usage/assets/staging/cursor_usage_events.sql`
- `template-sources/ai-coding-usage/dashboards/ai-coding-usage.yml`
- `template-sources/ai-coding-usage/pipeline.yml`

## athena
This pipeline template is designed for data processing workflows using Amazon Athena. It demonstrates how to use Bruin to define and execute SQL queries in Athena with...
Docs: `getting-started/templates-docs/athena-README.md`

- `template-sources/athena/assets/cars.sql`
- `template-sources/athena/assets/drivers.sql`
- `template-sources/athena/assets/payments.sql`
- `template-sources/athena/assets/travellers.sql`
- `template-sources/athena/pipeline.yml`

## bigquery

- `template-sources/bigquery/assets/example.sql`
- `template-sources/bigquery/assets/macro_example.sql`
- `template-sources/bigquery/assets/seed.asset.yml`
- `template-sources/bigquery/macros/aggregations.sql`
- `template-sources/bigquery/macros/filters.sql`
- `template-sources/bigquery/macros/transformations.sql`
- `template-sources/bigquery/pipeline.yml`

## bootstrap

- `template-sources/bootstrap/.bruin.yml`
- `template-sources/bootstrap/assets/bootstrap_v0.asset.yml`
- `template-sources/bootstrap/assets/bootstrap_v1.asset.yml`
- `template-sources/bootstrap/pipeline.yml`

## bronze-silver-postgres
The Bronze-to-Silver PostgreSQL template showcases how to pair a credential-free source with a relational
Docs: `getting-started/templates-docs/bronze-silver-postgres-README.md`

- `template-sources/bronze-silver-postgres/.bruin.yml`
- `template-sources/bronze-silver-postgres/assets/bronze_raw_data.asset.yml`
- `template-sources/bronze-silver-postgres/assets/silver_aggregated.sql`
- `template-sources/bronze-silver-postgres/pipeline.yml`

## bruin-cloud

- `template-sources/bruin-cloud/.bruin.yml`
- `template-sources/bruin-cloud/assets/assets.asset.yml`
- `template-sources/bruin-cloud/assets/pipeline_summary.sql`
- `template-sources/bruin-cloud/assets/pipelines.asset.yml`
- `template-sources/bruin-cloud/pipeline.yml`

## chargebee-bigquery
A Bruin pipeline that ingests Chargebee billing data into BigQuery and models it
Docs: `getting-started/templates-docs/chargebee-bigquery-README.md`

- `template-sources/chargebee-bigquery/.bruin.yml`
- `template-sources/chargebee-bigquery/assets/chargebee_raw/customer.asset.yml`
- `template-sources/chargebee-bigquery/assets/chargebee_raw/event.asset.yml`
- `template-sources/chargebee-bigquery/assets/chargebee_raw/invoice.asset.yml`
- `template-sources/chargebee-bigquery/assets/chargebee_raw/subscription.asset.yml`
- `template-sources/chargebee-bigquery/assets/chargebee_raw/transaction.asset.yml`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/failed_payment_dunning.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/monthly_invoice_billings.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/monthly_mrr_by_customer.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/monthly_mrr_movements.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/monthly_subscription_kpis.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/mrr_by_plan.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_reports/revenue_concentration.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_stage/customer_currency_daily_mrr_snapshot.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_stage/customers.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_stage/invoices.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_stage/subscription_items.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_stage/subscriptions.sql`
- `template-sources/chargebee-bigquery/assets/chargebee_stage/transactions.sql`
- `template-sources/chargebee-bigquery/dashboards/chargebee-billing-analytics.yml`
- `template-sources/chargebee-bigquery/macros/chargebee.sql`
- `template-sources/chargebee-bigquery/pipeline.yml`

## chess
This pipeline is a simple example of a Bruin pipeline. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/chess-README.md`

- `template-sources/chess/.bruin.yml`
- `template-sources/chess/assets/chess_games.asset.yml`
- `template-sources/chess/assets/chess_profiles.asset.yml`
- `template-sources/chess/assets/player_summary.sql`
- `template-sources/chess/pipeline.yml`

## clickhouse
This pipeline is a compact tour of Bruin on ClickHouse. It combines SQL transformations, a Python materialization, versioned seed data, a PostgreSQL source and sensor,...
Docs: `getting-started/templates-docs/clickhouse-README.md`

- `template-sources/clickhouse/.bruin.yml`
- `template-sources/clickhouse/assets/data_definitions/country_targets.asset.yml`
- `template-sources/clickhouse/assets/data_definitions/order_events_contract.sql`
- `template-sources/clickhouse/assets/ingestion/postgres_order_daily_monitor.sql`
- `template-sources/clickhouse/assets/ingestion/postgres_orders_sensor.asset.yml`
- `template-sources/clickhouse/assets/ingestion/postgres_orders_source.asset.yml`
- `template-sources/clickhouse/assets/ingestion/raw_postgres_orders.asset.yml`
- `template-sources/clickhouse/assets/materialization_types/country_revenue.sql`
- `template-sources/clickhouse/assets/materialization_types/country_revenue_leaderboard.sql`
- `template-sources/clickhouse/assets/materialization_types/customer_order_summary.sql`
- `template-sources/clickhouse/assets/materialization_types/daily_order_snapshot.sql`
- `template-sources/clickhouse/assets/materialization_types/order_change_log.sql`
- `template-sources/clickhouse/assets/materialization_types/pipeline_daily_snapshot.sql`
- `template-sources/clickhouse/assets/materialization_types/raw_customers.sql`
- `template-sources/clickhouse/assets/materialization_types/raw_orders.sql`
- `template-sources/clickhouse/assets/python/customer_regions.py`
- `template-sources/clickhouse/pipeline.yml`

## databricks

- `template-sources/databricks/assets/trips_summary_monthly.sql`
- `template-sources/databricks/pipeline.yml`

## default

- `template-sources/default/.bruin.yml`
- `template-sources/default/assets/my_python_asset.py`
- `template-sources/default/assets/player_stats.sql`
- `template-sources/default/assets/players.asset.yml`
- `template-sources/default/pipeline.yml`

## demo-payments-clickhouse
A self-contained demo template for near-real-time payments authorization and fraud
Docs: `getting-started/templates-docs/demo-payments-clickhouse-README.md`

- `template-sources/demo-payments-clickhouse/.bruin.yml`
- `template-sources/demo-payments-clickhouse/assets/ingestion/raw_transaction_changes.asset.yml`
- `template-sources/demo-payments-clickhouse/assets/ingestion/transactions_seed.py`
- `template-sources/demo-payments-clickhouse/assets/kpi/kpi_txn_daily.sql`
- `template-sources/demo-payments-clickhouse/assets/rollups/rollup_txn_1h.sql`
- `template-sources/demo-payments-clickhouse/assets/rollups/rollup_txn_1m.sql`
- `template-sources/demo-payments-clickhouse/assets/serving/serving_realtime_risk.sql`
- `template-sources/demo-payments-clickhouse/assets/staging/stg_transaction_changes.sql`
- `template-sources/demo-payments-clickhouse/dashboards/payments_risk.yml`
- `template-sources/demo-payments-clickhouse/demo.sh`
- `template-sources/demo-payments-clickhouse/docker/bruin-local.yml`
- `template-sources/demo-payments-clickhouse/docker/compose.yml`
- `template-sources/demo-payments-clickhouse/docker/postgres-init.sql`
- `template-sources/demo-payments-clickhouse/docs/ingestion-boundaries.md`
- `template-sources/demo-payments-clickhouse/docs/mode2-aggregating-mergetree.md`
- `template-sources/demo-payments-clickhouse/pipeline.yml`
- `template-sources/demo-payments-clickhouse/semantic/payments_risk.yml`

## demo-self-heal-pipeline
This project is a local DuckDB sandbox for testing Bruin agent troubleshooting skills. It has demo-seed to load realistic raw tables, then demo-pipeline with normal SQ...
Docs: `getting-started/templates-docs/demo-self-heal-pipeline-README.md`

- `template-sources/demo-self-heal-pipeline/.bruin.yml`
- `template-sources/demo-self-heal-pipeline/demo-pipeline/assets/daily_activity.sql`
- `template-sources/demo-self-heal-pipeline/demo-pipeline/assets/order_margin.sql`
- `template-sources/demo-self-heal-pipeline/demo-pipeline/assets/product_prices.sql`
- `template-sources/demo-self-heal-pipeline/demo-pipeline/assets/staging_orders.sql`
- `template-sources/demo-self-heal-pipeline/demo-pipeline/assets/status_snapshot.sql`
- `template-sources/demo-self-heal-pipeline/demo-pipeline/pipeline.yml`
- `template-sources/demo-self-heal-pipeline/demo-seed/assets/fulfillment_events.asset.yml`
- `template-sources/demo-self-heal-pipeline/demo-seed/assets/order_adjustments.asset.yml`
- `template-sources/demo-self-heal-pipeline/demo-seed/assets/order_status_history.asset.yml`
- `template-sources/demo-self-heal-pipeline/demo-seed/assets/orders.asset.yml`
- `template-sources/demo-self-heal-pipeline/demo-seed/assets/product_catalog.asset.yml`
- `template-sources/demo-self-heal-pipeline/demo-seed/pipeline.yml`

## demo-snowflake-sales-analytics
This template creates an end-to-end Snowflake analytics demo with dummy retail sales data.
Docs: `getting-started/templates-docs/demo-snowflake-sales-analytics-README.md`

- `template-sources/demo-snowflake-sales-analytics/.bruin.yml`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/distribution_points.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/inventory_snapshots.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/product_costs.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/products.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/retailers.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/sales_transactions.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/sku_market_availability.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/stores.py`
- `template-sources/demo-snowflake-sales-analytics/assets/bronze/trade_promotions.py`
- `template-sources/demo-snowflake-sales-analytics/assets/gold/channel_opportunity_alerts.sql`
- `template-sources/demo-snowflake-sales-analytics/assets/gold/limited_edition_decision_board.sql`
- `template-sources/demo-snowflake-sales-analytics/assets/gold/sku_decision_drivers.sql`
- `template-sources/demo-snowflake-sales-analytics/assets/gold/weekly_sku_council_summary.sql`
- `template-sources/demo-snowflake-sales-analytics/assets/silver/limited_edition_performance.sql`
- `template-sources/demo-snowflake-sales-analytics/assets/silver/retailer_channel_scorecard.sql`
- `template-sources/demo-snowflake-sales-analytics/assets/silver/sku_daily_sales.sql`
- `template-sources/demo-snowflake-sales-analytics/pipeline.yml`

## demo-snowflake-salesforce
This template creates an end-to-end demo pipeline for a credit union CRM analytics use case.
Docs: `getting-started/templates-docs/demo-snowflake-salesforce-README.md`

- `template-sources/demo-snowflake-salesforce/.bruin.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/requirements.txt`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_accounts.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_campaign_members.sql`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_campaigns.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_contacts.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_events.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_leads.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_opportunities.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_opportunity_contact_roles.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_opportunity_line_items.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_pricebook_entries.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_pricebooks.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_products.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_tasks.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/salesforce_users.asset.yml`
- `template-sources/demo-snowflake-salesforce/assets/bronze/seed_salesforce_demo_data.py`
- `template-sources/demo-snowflake-salesforce/assets/gold/activity_coverage_by_product.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/banker_activity_coverage.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/branch_relationship_health.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/campaign_conversion_funnel.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/pipeline_by_channel_daily.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/pipeline_by_channel_monthly.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/pipeline_by_stage.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/pipeline_kpis.sql`
- `template-sources/demo-snowflake-salesforce/assets/gold/product_pipeline_performance.sql`
- `template-sources/demo-snowflake-salesforce/assets/silver/salesforce_account_health.sql`
- `template-sources/demo-snowflake-salesforce/assets/silver/salesforce_activity_timeline.sql`
- `template-sources/demo-snowflake-salesforce/assets/silver/salesforce_marketing_funnel.sql`
- `template-sources/demo-snowflake-salesforce/assets/silver/salesforce_opportunity_pipeline.sql`
- `template-sources/demo-snowflake-salesforce/assets/silver/salesforce_product_pipeline.sql`
- `template-sources/demo-snowflake-salesforce/pipeline.yml`

## duckdb
This pipeline is a simple example of a Bruin pipeline for DuckDB,
Docs: `getting-started/templates-docs/duckdb-README.md`

- `template-sources/duckdb/.bruin.yml`
- `template-sources/duckdb/assets/example.sql`
- `template-sources/duckdb/assets/macro_example.sql`
- `template-sources/duckdb/assets/seed.asset.yml`
- `template-sources/duckdb/macros/aggregations.sql`
- `template-sources/duckdb/macros/filters.sql`
- `template-sources/duckdb/macros/transformations.sql`
- `template-sources/duckdb/pipeline.yml`

## duckdb-example

- `template-sources/duckdb-example/assets/product_categories.sql`
- `template-sources/duckdb-example/assets/product_price_summary.sql`
- `template-sources/duckdb-example/assets/products.sql`
- `template-sources/duckdb-example/assets/shipping_providers.sql`
- `template-sources/duckdb-example/pipeline.yml`

## duckdb-lineage

- `template-sources/duckdb-lineage/.bruin.yml`
- `template-sources/duckdb-lineage/assets/country.sql`
- `template-sources/duckdb-lineage/assets/example.sql`
- `template-sources/duckdb-lineage/assets/people.sql`
- `template-sources/duckdb-lineage/assets/users.sql`
- `template-sources/duckdb-lineage/pipeline.yml`

## ecommerce
The ecommerce template is an interactive template that scaffolds a complete ecommerce analytics pipeline. It sets up raw ingestion from your selected sources, a stagin...
Docs: `getting-started/templates-docs/ecommerce-README.md`

- `template-sources/ecommerce/assets/raw/facebook_ad_insights.asset.yml`
- `template-sources/ecommerce/assets/raw/facebook_campaigns.asset.yml`
- `template-sources/ecommerce/assets/raw/ga4_events.asset.yml`
- `template-sources/ecommerce/assets/raw/ga4_sessions.asset.yml`
- `template-sources/ecommerce/assets/raw/google_ad_insights.asset.yml`
- `template-sources/ecommerce/assets/raw/google_campaigns.asset.yml`
- `template-sources/ecommerce/assets/raw/hubspot_campaigns.asset.yml`
- `template-sources/ecommerce/assets/raw/hubspot_contacts.asset.yml`
- `template-sources/ecommerce/assets/raw/hubspot_deals.asset.yml`
- `template-sources/ecommerce/assets/raw/klaviyo_campaigns.asset.yml`
- `template-sources/ecommerce/assets/raw/klaviyo_flows.asset.yml`
- `template-sources/ecommerce/assets/raw/klaviyo_metrics.asset.yml`
- `template-sources/ecommerce/assets/raw/mixpanel_events.asset.yml`
- `template-sources/ecommerce/assets/raw/mixpanel_funnels.asset.yml`
- `template-sources/ecommerce/assets/raw/shopify_customers.asset.yml`
- `template-sources/ecommerce/assets/raw/shopify_inventory.asset.yml`
- `template-sources/ecommerce/assets/raw/shopify_orders.asset.yml`
- `template-sources/ecommerce/assets/raw/shopify_products.asset.yml`
- `template-sources/ecommerce/assets/raw/stripe_charges.asset.yml`
- `template-sources/ecommerce/assets/raw/stripe_customers.asset.yml`
- `template-sources/ecommerce/assets/raw/stripe_payouts.asset.yml`
- `template-sources/ecommerce/assets/raw/stripe_refunds.asset.yml`
- `template-sources/ecommerce/assets/raw/tiktok_ad_insights.asset.yml`
- `template-sources/ecommerce/assets/raw/tiktok_campaigns.asset.yml`
- `template-sources/ecommerce/assets/reports/rpt_customer_cohorts.sql.tmpl`
- `template-sources/ecommerce/assets/reports/rpt_daily_kpis.sql.tmpl`
- `template-sources/ecommerce/assets/reports/rpt_daily_revenue.sql.tmpl`
- `template-sources/ecommerce/assets/reports/rpt_marketing_roi.sql.tmpl`
- `template-sources/ecommerce/assets/reports/rpt_product_performance.sql`
- `template-sources/ecommerce/assets/staging/stg_customers.sql.tmpl`
- `template-sources/ecommerce/assets/staging/stg_marketing_spend.sql.tmpl`
- `template-sources/ecommerce/assets/staging/stg_orders.sql.tmpl`
- `template-sources/ecommerce/assets/staging/stg_products.sql`
- `template-sources/ecommerce/assets/staging/stg_web_sessions.sql.tmpl`
- `template-sources/ecommerce/manifest.yml`
- `template-sources/ecommerce/pipeline.yml.tmpl`

## empty

- `template-sources/empty/assets/placeholder`
- `template-sources/empty/pipeline.yml`

## firebase
This pipeline is a simple example of a Bruin pipeline for Firebase.
Docs: `getting-started/templates-docs/firebase-README.md`

- `template-sources/firebase/assets/analytics_123456789/events.asset.yaml`
- `template-sources/firebase/assets/analytics_123456789/events_intraday.asset.yaml`
- `template-sources/firebase/assets/analytics_123456789/parse_version.sql`
- `template-sources/firebase/assets/events/events.sql`
- `template-sources/firebase/assets/events/events_json.sql`
- `template-sources/firebase/assets/events/stg_events.sql`
- `template-sources/firebase/assets/user_model/stg_users_daily.sql`
- `template-sources/firebase/assets/user_model/users.sql`
- `template-sources/firebase/assets/user_model/users_daily.sql`
- `template-sources/firebase/pipeline.yml`
- `template-sources/firebase/queries/event_params.sql`

## frankfurter
This pipeline is a simple example of a Bruin pipeline. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/frankfurter-README.md`

- `template-sources/frankfurter/.bruin.yml`
- `template-sources/frankfurter/assets/frankfurter/currency_names.sql`
- `template-sources/frankfurter/assets/frankfurter/daily_rates.sql`
- `template-sources/frankfurter/assets/frankfurter_raw/currencies.asset.yml`
- `template-sources/frankfurter/assets/frankfurter_raw/rates.asset.yml`
- `template-sources/frankfurter/assets/fx_insights/currency_performance.sql`
- `template-sources/frankfurter/pipeline.yml`

## google-web-analytics
google-web-analytics turns the GA4 and Google Search Console exports you already
Docs: `getting-started/templates-docs/google-web-analytics-README.md`

- `template-sources/google-web-analytics/.bruin.yml`
- `template-sources/google-web-analytics/assets/web_analytics_raw/ga4_events_intraday.asset.yml`
- `template-sources/google-web-analytics/assets/web_analytics_raw/gsc_export_log.asset.yml`
- `template-sources/google-web-analytics/assets/web_analytics_raw/gsc_searchdata_site_impression.asset.yml`
- `template-sources/google-web-analytics/assets/web_analytics_raw/gsc_searchdata_url_impression.asset.yml`
- `template-sources/google-web-analytics/assets/web_analytics_reports/ga4_gsc_intent_pipeline.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/ga4_gsc_landing_page_performance.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/ga4_gsc_query_value.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/gsc_brand_split_weekly.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/gsc_competitor_visibility.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/gsc_new_and_lost_queries.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/gsc_page_trend.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/gsc_query_cannibalization.sql`
- `template-sources/google-web-analytics/assets/web_analytics_reports/gsc_query_opportunities.sql`
- `template-sources/google-web-analytics/assets/web_analytics_staging/ga4_page_daily.sql`
- `template-sources/google-web-analytics/assets/web_analytics_staging/ga4_sessions.sql`
- `template-sources/google-web-analytics/assets/web_analytics_staging/gsc_export_log.sql`
- `template-sources/google-web-analytics/assets/web_analytics_staging/gsc_position_click_curve.sql`
- `template-sources/google-web-analytics/assets/web_analytics_staging/gsc_site_query_daily.sql`
- `template-sources/google-web-analytics/assets/web_analytics_staging/gsc_url_query_daily.sql`
- `template-sources/google-web-analytics/dashboards/01-overview.yml`
- `template-sources/google-web-analytics/dashboards/02-ga4-insights.yml`
- `template-sources/google-web-analytics/dashboards/03-gsc-insights.yml`
- `template-sources/google-web-analytics/macros/search.sql`
- `template-sources/google-web-analytics/macros/url.sql`
- `template-sources/google-web-analytics/pipeline.yml`

## gorgias
This pipeline is a simple example of a Bruin pipeline that copies data from Gorgias to BigQuery. It copies data from the following resources:
Docs: `getting-started/templates-docs/gorgias-README.md`

- `template-sources/gorgias/assets/customers.asset.yml`
- `template-sources/gorgias/assets/satisfaction_surveys.asset.yml`
- `template-sources/gorgias/assets/ticket_messages.asset.yml`
- `template-sources/gorgias/assets/tickets.asset.yml`
- `template-sources/gorgias/pipeline.yml`

## gsheet-bigquery
This pipeline is a simple example of a Bruin pipeline that copies data from GSheet to BigQuery. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/gsheet-bigquery-README.md`

- `template-sources/gsheet-bigquery/assets/gsheet.asset.yml`
- `template-sources/gsheet-bigquery/pipeline.yml`

## gsheet-duckdb
This pipeline is a simple example of a Bruin pipeline that copies data from GSheet to DuckDB. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/gsheet-duckdb-README.md`

- `template-sources/gsheet-duckdb/assets/gsheet.asset.yml`
- `template-sources/gsheet-duckdb/pipeline.yml`

## iceberg-glue-s3
Loads two tables from Frankfurter, a public exchange-rate API, into Apache Iceberg tables catalogued in AWS Glue with the data in S3. This is the shape most AWS deploy...
Docs: `getting-started/templates-docs/iceberg-glue-s3-README.md`

- `template-sources/iceberg-glue-s3/.bruin.yml`
- `template-sources/iceberg-glue-s3/assets/raw/currencies.asset.yml`
- `template-sources/iceberg-glue-s3/assets/raw/exchange_rates.asset.yml`
- `template-sources/iceberg-glue-s3/pipeline.yml`

## iceberg-hadoop-gcsinterop
Loads two tables from Frankfurter, a public exchange-rate API, into Apache Iceberg tables that need no catalog service at all. The hadoop catalog keeps its metadata in...
Docs: `getting-started/templates-docs/iceberg-hadoop-gcsinterop-README.md`

- `template-sources/iceberg-hadoop-gcsinterop/.bruin.yml`
- `template-sources/iceberg-hadoop-gcsinterop/assets/raw/currencies.asset.yml`
- `template-sources/iceberg-hadoop-gcsinterop/assets/raw/exchange_rates.asset.yml`
- `template-sources/iceberg-hadoop-gcsinterop/pipeline.yml`

## iceberg-postgres-gcs
Loads two tables from Frankfurter, a public exchange-rate API, into Apache Iceberg tables catalogued in Postgres with the data in Google Cloud Storage. Useful on GCP,...
Docs: `getting-started/templates-docs/iceberg-postgres-gcs-README.md`

- `template-sources/iceberg-postgres-gcs/.bruin.yml`
- `template-sources/iceberg-postgres-gcs/assets/raw/currencies.asset.yml`
- `template-sources/iceberg-postgres-gcs/assets/raw/exchange_rates.asset.yml`
- `template-sources/iceberg-postgres-gcs/pipeline.yml`

## iceberg-rest-minio
Loads two tables from Frankfurter, a public exchange-rate API, into Apache Iceberg — with a real catalog server in front of real object storage, both running locally i...
Docs: `getting-started/templates-docs/iceberg-rest-minio-README.md`

- `template-sources/iceberg-rest-minio/.bruin.yml`
- `template-sources/iceberg-rest-minio/assets/raw/currencies.asset.yml`
- `template-sources/iceberg-rest-minio/assets/raw/exchange_rates.asset.yml`
- `template-sources/iceberg-rest-minio/docker-compose.yml`
- `template-sources/iceberg-rest-minio/pipeline.yml`

## iceberg-sqlite-local
Loads two tables from Frankfurter, a public exchange-rate API, into Apache Iceberg tables on your own disk. No cloud account, no credentials, no services to start.
Docs: `getting-started/templates-docs/iceberg-sqlite-local-README.md`

- `template-sources/iceberg-sqlite-local/.bruin.yml`
- `template-sources/iceberg-sqlite-local/assets/raw/currencies.asset.yml`
- `template-sources/iceberg-sqlite-local/assets/raw/exchange_rates.asset.yml`
- `template-sources/iceberg-sqlite-local/pipeline.yml`

## migration-fivetran

- `template-sources/migration-fivetran/.agents/skills/bruin-fivetran-migrator/SKILL.md`
- `template-sources/migration-fivetran/.agents/skills/bruin-fivetran-migrator/import_fivetran.py`
- `template-sources/migration-fivetran/bruin/assets/placeholder`
- `template-sources/migration-fivetran/bruin/pipeline.yml`
- `template-sources/migration-fivetran/fivetran-bruin-prompt.md`
- `template-sources/migration-fivetran/plan.md`

## notion
This pipeline is a simple example of a Bruin pipeline that copies data from Notion to BigQuery. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/notion-README.md`

- `template-sources/notion/assets/example.sql`
- `template-sources/notion/assets/notion.asset.yml`
- `template-sources/notion/pipeline.yml`

## nyc-taxi

- `template-sources/nyc-taxi/.bruin.yml`
- `template-sources/nyc-taxi/assets/raw/payment_lookup.asset.yml`
- `template-sources/nyc-taxi/assets/raw/taxi_zone_lookup.sql`
- `template-sources/nyc-taxi/assets/raw/trips_raw.py`
- `template-sources/nyc-taxi/assets/reports/report_trips_monthly.sql`
- `template-sources/nyc-taxi/assets/staging/trips_summary.sql`
- `template-sources/nyc-taxi/pipeline.yml`
- `template-sources/nyc-taxi/requirements.txt`

## oracle-duckdb

- `template-sources/oracle-duckdb/.bruin.yml`
- `template-sources/oracle-duckdb/assets/oracle_customers.asset.yml`
- `template-sources/oracle-duckdb/assets/oracle_order_items.asset.yml`
- `template-sources/oracle-duckdb/assets/oracle_orders.asset.yml`
- `template-sources/oracle-duckdb/assets/sales_per_customer.sql`
- `template-sources/oracle-duckdb/pipeline.yml`

## posthog-bigquery
posthog-bigquery turns raw PostHog product analytics into warehouse-ready
Docs: `getting-started/templates-docs/posthog-bigquery-README.md`

- `template-sources/posthog-bigquery/.bruin.yml`
- `template-sources/posthog-bigquery/assets/posthog_raw/events.asset.yml`
- `template-sources/posthog-bigquery/assets/posthog_raw/feature_flags.asset.yml`
- `template-sources/posthog-bigquery/assets/posthog_raw/persons.asset.yml`
- `template-sources/posthog-bigquery/assets/posthog_reports/account_engagement_monthly.sql`
- `template-sources/posthog-bigquery/assets/posthog_reports/feature_adoption_by_segment.sql`
- `template-sources/posthog-bigquery/assets/posthog_reports/product_qualified_accounts.sql`
- `template-sources/posthog-bigquery/assets/posthog_reports/weekly_retention_cohorts.sql`
- `template-sources/posthog-bigquery/assets/posthog_stage/accounts.sql`
- `template-sources/posthog-bigquery/assets/posthog_stage/events.sql`
- `template-sources/posthog-bigquery/assets/posthog_stage/feature_flag_exposures.sql`
- `template-sources/posthog-bigquery/assets/posthog_stage/person_distinct_ids.sql`
- `template-sources/posthog-bigquery/assets/posthog_stage/persons.sql`
- `template-sources/posthog-bigquery/assets/posthog_stage/sessions.sql`
- `template-sources/posthog-bigquery/dashboards/posthog-product-analytics.yml`
- `template-sources/posthog-bigquery/macros/posthog.sql`
- `template-sources/posthog-bigquery/pipeline.yml`

## python
This pipeline is a simple example of a Bruin pipeline. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/python-README.md`

- `template-sources/python/.bruin.yml`
- `template-sources/python/assets/mat/asset.py`
- `template-sources/python/assets/mat/requirements.txt`
- `template-sources/python/assets/python311/asset.py`
- `template-sources/python/assets/python312/asset.py`
- `template-sources/python/assets/python313/asset.py`
- `template-sources/python/assets/python313/requirements.txt`
- `template-sources/python/pipeline.yml`
- `template-sources/python/requirements.txt`

## quickbooks-bigquery
quickbooks-bigquery is a focused QuickBooks Online pipeline for BigQuery. It loads seven QuickBooks Accounting API objects into the quickbooksraw dataset with ingestr,...
Docs: `getting-started/templates-docs/quickbooks-bigquery-README.md`

- `template-sources/quickbooks-bigquery/.bruin.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/accounts.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/bills.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/customers.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/invoices.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/payments.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/purchases.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_raw/vendors.asset.yml`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/accounts.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/bills.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/customers.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/expense_lines.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/invoice_lines.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/invoices.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/payment_applications.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/payments.sql`
- `template-sources/quickbooks-bigquery/assets/quickbooks_stage/vendors.sql`
- `template-sources/quickbooks-bigquery/pipeline.yml`

## r

- `template-sources/r/.bruin.yml`
- `template-sources/r/assets/basic/analysis.r`
- `template-sources/r/assets/with-deps/data_viz.r`
- `template-sources/r/assets/with-deps/renv.lock`
- `template-sources/r/pipeline.yml`

## redshift

- `template-sources/redshift/assets/example.sql`
- `template-sources/redshift/pipeline.yml`

## shopify-bigquery
This pipeline is a simple example of a Bruin pipeline that copies data from Shopify to BigQuery. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/shopify-bigquery-README.md`

- `template-sources/shopify-bigquery/assets/shopify.customers.asset.yml`
- `template-sources/shopify-bigquery/assets/shopify.discounts.asset.yml`
- `template-sources/shopify-bigquery/assets/shopify.events.asset.yml`
- `template-sources/shopify-bigquery/assets/shopify.inventory_items.asset.yml`
- `template-sources/shopify-bigquery/assets/shopify.orders.asset.yml`
- `template-sources/shopify-bigquery/assets/shopify.price_rules.asset.yml`
- `template-sources/shopify-bigquery/assets/shopify.products.asset.yml`
- `template-sources/shopify-bigquery/pipeline.yml`

## shopify-clickhouse
This template builds a Shopify analytics pipeline with Bruin, ingestr, and ClickHouse. It ingests Shopify customers, products, orders, inventory items, discounts, and...
Docs: `getting-started/templates-docs/shopify-clickhouse-README.md`

- `template-sources/shopify-clickhouse/assets/t1/t1_customers.asset.yml`
- `template-sources/shopify-clickhouse/assets/t1/t1_discounts.asset.yml`
- `template-sources/shopify-clickhouse/assets/t1/t1_events.asset.yml`
- `template-sources/shopify-clickhouse/assets/t1/t1_inventory_items.asset.yml`
- `template-sources/shopify-clickhouse/assets/t1/t1_orders.asset.yml`
- `template-sources/shopify-clickhouse/assets/t1/t1_products.asset.yml`
- `template-sources/shopify-clickhouse/assets/t2/t2_customers.sql`
- `template-sources/shopify-clickhouse/assets/t2/t2_inventory_items.sql`
- `template-sources/shopify-clickhouse/assets/t2/t2_order_line_items.sql`
- `template-sources/shopify-clickhouse/assets/t2/t2_orders.sql`
- `template-sources/shopify-clickhouse/assets/t2/t2_products.sql`
- `template-sources/shopify-clickhouse/assets/t3/t3_customer_cohorts.sql`
- `template-sources/shopify-clickhouse/assets/t3/t3_daily_kpis.sql`
- `template-sources/shopify-clickhouse/assets/t3/t3_daily_revenue.sql`
- `template-sources/shopify-clickhouse/assets/t3/t3_payment_reconciliation.sql`
- `template-sources/shopify-clickhouse/assets/t3/t3_product_performance.sql`
- `template-sources/shopify-clickhouse/pipeline.yml`

## shopify-duckdb
This pipeline is a simple example of a Bruin pipeline that copies data from Shopify to DuckDB. It demonstrates how to use the bruin CLI to build and run a pipeline.
Docs: `getting-started/templates-docs/shopify-duckdb-README.md`

- `template-sources/shopify-duckdb/assets/shopify.customers.asset.yml`
- `template-sources/shopify-duckdb/assets/shopify.discounts.asset.yml`
- `template-sources/shopify-duckdb/assets/shopify.events.asset.yml`
- `template-sources/shopify-duckdb/assets/shopify.inventory_items.asset.yml`
- `template-sources/shopify-duckdb/assets/shopify.orders.asset.yml`
- `template-sources/shopify-duckdb/assets/shopify.price_rules.asset.yml`
- `template-sources/shopify-duckdb/assets/shopify.products.asset.yml`
- `template-sources/shopify-duckdb/pipeline.yml`

## stripe-bigquery
stripe-bigquery is a focused Stripe billing analytics pipeline for BigQuery. It loads the customer, product, price, subscription, subscription-item, and invoice resour...
Docs: `getting-started/templates-docs/stripe-bigquery-README.md`

- `template-sources/stripe-bigquery/.bruin.yml`
- `template-sources/stripe-bigquery/assets/stripe_raw/customer.asset.yml`
- `template-sources/stripe-bigquery/assets/stripe_raw/invoice.asset.yml`
- `template-sources/stripe-bigquery/assets/stripe_raw/price.asset.yml`
- `template-sources/stripe-bigquery/assets/stripe_raw/product.asset.yml`
- `template-sources/stripe-bigquery/assets/stripe_raw/subscription.asset.yml`
- `template-sources/stripe-bigquery/assets/stripe_raw/subscription_item.asset.yml`
- `template-sources/stripe-bigquery/assets/stripe_reports/monthly_invoice_billings.sql`
- `template-sources/stripe-bigquery/assets/stripe_reports/monthly_mrr_by_customer.sql`
- `template-sources/stripe-bigquery/assets/stripe_reports/monthly_mrr_movements.sql`
- `template-sources/stripe-bigquery/assets/stripe_reports/monthly_subscription_kpis.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/customer_currency_daily_mrr_snapshot.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/customers.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/invoice_line_items.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/invoices.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/prices.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/products.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/subscription_item_daily_snapshot.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/subscription_items.sql`
- `template-sources/stripe-bigquery/assets/stripe_stage/subscriptions.sql`
- `template-sources/stripe-bigquery/dashboards/stripe-billing-analytics.yml`
- `template-sources/stripe-bigquery/pipeline.yml`

## stripe-databricks

- `template-sources/stripe-databricks/assets/bronze/bronze_balance_transaction_data_raw.asset.yml`
- `template-sources/stripe-databricks/assets/bronze/bronze_charge_data_raw.asset.yml`
- `template-sources/stripe-databricks/assets/bronze/bronze_customer_data_raw.asset.yml`
- `template-sources/stripe-databricks/assets/bronze/bronze_subscription_data_raw.asset.yml`
- `template-sources/stripe-databricks/assets/silver/silver_customer_subscription_simple.sql`
- `template-sources/stripe-databricks/pipeline.yml`

## variant-example

- `template-sources/variant-example/.bruin.yml`
- `template-sources/variant-example/assets/raw_users.sql`
- `template-sources/variant-example/assets/regional_snapshot.sql`
- `template-sources/variant-example/assets/requirements.txt`
- `template-sources/variant-example/assets/seed.py`
- `template-sources/variant-example/assets/users_summary.sql`
- `template-sources/variant-example/pipeline.yml`

## zoomcamp

- `template-sources/zoomcamp/.bruin.yml`
- `template-sources/zoomcamp/pipeline/assets/ingestion/payment_lookup.asset.yml`
- `template-sources/zoomcamp/pipeline/assets/ingestion/requirements.txt`
- `template-sources/zoomcamp/pipeline/assets/ingestion/trips.py`
- `template-sources/zoomcamp/pipeline/assets/reports/trips_report.sql`
- `template-sources/zoomcamp/pipeline/assets/staging/trips.sql`
- `template-sources/zoomcamp/pipeline/pipeline.yml`

