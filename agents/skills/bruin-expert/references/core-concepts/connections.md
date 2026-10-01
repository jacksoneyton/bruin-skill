# Connections

Connections are sets of credentials that enable Bruin to communicate with external platforms. They are configured within your [project's](project.md) `.bruin.yml` file.

## Overview

Bruin supports connections to:

- **Data Platforms**: Where your data is stored and transformed (BigQuery, Snowflake, PostgreSQL, etc.)
- **Ingestion Sources**: Where data is loaded from (Shopify, HubSpot, Stripe, etc.)

## Connection Structure

Connections are defined within an environment under the `connections` key, grouped by connection type:

```yaml
environments:
  default:
    connections:
      # Data platform connection
      google_cloud_platform:
        - name: "gcp-prod"
          project_id: "my-project"
          service_account_file: "credentials/gcp-service-account.json"
      
      # Database connection
      postgres:
        - name: "postgres-main"
          username: "bruin_user"
          password: "super_secret"
          host: "db.example.com"
          port: 5432
          database: "analytics"
      
      # Ingestion source connection
      shopify:
        - name: "shopify-default"
          api_key: "shpca_abc123"
          store_name: "my-store"
```

> [!NOTE]
> You can reference environment variables in connection fields using `${VAR_NAME}` placeholders, which are expanded at runtime.

## Connection Names

Each connection has a unique `name` that you reference in your pipeline and asset definitions:

```yaml
# pipeline.yml
default_connections:
  google_cloud_platform: "gcp-prod"
  postgres: "postgres-main"
```

```yaml
# asset.yml
name: raw.orders
type: ingestr
parameters:
  source_connection: shopify-default
  destination: postgres
```

## Default Connections

Pipelines can define default connections that are automatically used by assets of that type:

```yaml
# pipeline.yml
name: analytics-daily
default_connections:
  google_cloud_platform: "gcp-prod"
  snowflake: "sf-default"
  postgres: "pg-default"
```

Assets automatically inherit these connections unless they specify a different one.

## Limiting Connection Concurrency

If a connection should only be used by a limited number of assets at once, set `max_concurrent_assets` on that connection in `.bruin.yml`:

```yaml
environments:
  default:
    connections:
      snowflake:
        - name: "sf-default"
          account: "ABC12345"
          username: "bruin_user"
          private_key_path: "credentials/snowflake_key.p8"
          database: "ANALYTICS"
          warehouse: "COMPUTE_WH"
          max_concurrent_assets: 4
```

Bruin will queue additional assets that need `sf-default` until a slot is available. This is useful when a database, warehouse, or API has a lower concurrency limit than the overall run's worker count. See [Concurrency & Resource Limits](../getting-started/concurrency.md#connection-concurrency-limits) for details.

## Data Platform Connections

For specific connection fields and configuration options, see the dedicated documentation:

| Connection Type | Documentation |
|----------------|---------------|
| `google_cloud_platform` | [Google BigQuery](../platforms/bigquery.md) |
| `snowflake` | [Snowflake](../platforms/snowflake.md) |
| `postgres` | [PostgreSQL](../platforms/postgres.md) |
| `redshift` | [Redshift](../platforms/redshift.md) |
| `databricks` | [Databricks](../platforms/databricks.md) |
| `athena` | [AWS Athena](../platforms/athena.md) |
| `duckdb` | [DuckDB](../platforms/duckdb.md) |
| `motherduck` | [MotherDuck](../platforms/motherduck.md) |
| `clickhouse` | [ClickHouse](../platforms/clickhouse.md) |
| `mysql` | [MySQL](../platforms/mysql.md) |
| `doris` | [Apache Doris](../platforms/doris.md) |
| `mssql` | [Microsoft SQL Server](../platforms/mssql.md) |
| `synapse` | [Azure Synapse](../platforms/synapse.md) |
| `oracle` | [Oracle](../platforms/oracle.md) |
| `trino` | [Trino](../platforms/trino.md) |
| `dremio` | [Dremio](../platforms/dremio.md) |
| `sail` | [Sail](../platforms/sail.md) |
| `spark` | [Apache Spark](../platforms/spark.md) |
| `s3` | [S3](../platforms/s3.md) |
| `gcs` | [Google Cloud Storage](../platforms/gcs.md) |

## Ingestion Source Connections

Connection schemas for ingestion sources are documented on their respective pages under [Data Ingestion](../ingestion/overview.md). Each source page includes the required `.bruin.yml` connection configuration.

## Testing Connections

Use the `connections` command to verify your connections:

```bash
# List all connections
bruin connections list

# Test a specific connection
bruin connections test --name gcp-prod
```

## Related Topics

- [Project](project.md) - Configure your project and environments
- [Secrets](secrets.md) - Manage custom credentials
- [.bruin.yml Reference](../secrets/bruinyml.md) - Complete configuration reference
