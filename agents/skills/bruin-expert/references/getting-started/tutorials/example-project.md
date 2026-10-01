# Explore Example Project

This tutorial ships as a single Bruin project with two pipelines side by side:

- **`chess-basic/`** — a minimal "hello world" pipeline: connections, one `pipeline.yml`, a couple of ingestr assets, and a single SQL report. A great first look at Bruin.
- **`chess-advance/`** — the same chess dataset expanded into a tour of Bruin's features: sensors, seeds, Python materialization, incremental SQL, the Python SDK, column & custom checks, custom variables, scheduling, notifications, and dashboards.

Both pipelines share the root `.bruin.yml` (connections) and `.gitignore`. Browse the tree on the left to explore each file.

*(interactive file viewer omitted; see references/template-sources/)*

## What's inside `chess-basic/`

- **`pipeline.yml`** — `name: chess_basic`, with `type: ingestr` as the default asset type.
- **`assets/raw/games.asset.yml`**, **`profiles.asset.yml`** — Ingestr assets that pull the Chess.com `games` and `profiles` endpoints into DuckDB.
- **`assets/reports/player_summary.sql`** — A single SQL report that joins and aggregates into a player-level win-rate table with one column check.

That's it — enough to run an end-to-end ingest + transform flow locally.

## What's inside `chess-advance/`

- **`pipeline.yml`** — `name: chess_advance`, plus pipeline-level `schedule`, `retries`, `concurrency`, `notifications`, `tags`, `default_connections`, and **custom variables** (`min_games`, `rating_category`).
- **`assets/raw/`** — Raw landing layer: ingestion and seeds.
  - **`ingestr_games.asset.yml`**, **`ingestr_profiles.asset.yml`** — Ingestr assets that inherit `type: ingestr` from pipeline defaults.
  - **`seed_top_players.asset.yml`** (+ `seed_top_players.csv`) — `duckdb.seed` loading static CSV data, with an `accepted_values` column check.
- **`assets/sensor/`** — Readiness gates.
  - **`sensor_games_ready.asset.yml`** — `duckdb.sensor.query` that polls until games have landed before downstream work runs.
- **`assets/transformations/`** — Intermediate processing.
  - **`python_materialization_player_ratings.py`** — Python asset with `materialize()` that returns a DataFrame to be written as a table; also reads the `rating_category` custom variable from `BRUIN_VARS`.
  - **`incremental_sql_daily_games.sql`** — Incremental SQL (`delete+insert` keyed on `game_date`) showcasing the built-in <code v-pre>{{ start_date }}</code> / <code v-pre>{{ end_date }}</code> variables.
- **`assets/reports/`** — Consumer-facing outputs.
  - **`sql_with_checks_player_summary.sql`** — Aggregate table demonstrating column checks (`not_null`, `unique`, `positive`, `min`, `max`), `custom_checks` with `value` / `blocking`, and the <code v-pre>{{ var.min_games }}</code> custom variable.
  - **`python_sdk_rating_insights.py`** — Bruin Python SDK **+** Python materialization combined. Uses `from bruin import query, context` to pull data from the warehouse and returns the enriched DataFrame from `materialize()` so Bruin writes it back as a table. Reads both built-in (`context.start_date`) and custom (`context.vars["min_games"]`) variables.
  - **`dashboard_chess_overview.asset.yml`** — `tableau` dashboard asset that appears as a terminal node in lineage.

## Setup

Save the files shown above into a directory with the same structure, and run the commands below from that directory. It must be inside a Git repository; if this is a new standalone project, run `git init` first.

Fill in `.bruin.yml` with your connections. You can read more about connections [here](../../connections/overview.md).

Both pipelines share the pre-configured list of 10 popular Chess.com players. You can modify the `players` list in your chess connection to track different players.

## Running a Pipeline

Run a whole pipeline by pointing at its folder:

```shell
bruin run chess-basic
# First advanced run: create the incremental table before updating it.
bruin run --workers 1 --full-refresh chess-advance
```

Use `--workers 1` for the advanced pipeline because its seed, ingestion, and Python assets share one DuckDB file. After the first successful run, use `bruin run --workers 1 chess-advance` for incremental runs. The Python dependencies are declared in `chess-advance/requirements.txt` and installed by Bruin.

Or run a single asset:

```shell
bruin run chess-advance/assets/reports/sql_with_checks_player_summary.sql
```

Override a custom variable for a single run (chess-advance only):

```shell
bruin run --workers 1 --var min_games=250 --var rating_category='"blitz"' chess-advance
```

You can optionally pass a `--downstream` flag to run an asset with all of its downstreams.
