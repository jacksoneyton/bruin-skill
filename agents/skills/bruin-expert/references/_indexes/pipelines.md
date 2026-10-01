# Index: Pipelines

3 pages. Paths are relative to references/.

- `getting-started/concurrency.md` | Concurrency & Resource Limits: Bruin runs assets in parallel based on their dependencies. Assets without dependencies on each other execute simultaneously.
- `pipelines/definition.md` | Pipeline Definition: A pipeline is a group of assets that are executed together in the right order. For instance, if you have an asset that ingests data from an API, and another one that c...
- `pipelines/variants.md` | Pipeline Variants: Variants let a single pipeline.yml produce multiple concrete pipelines from one source file. Each variant overrides a subset of the pipeline's custom variables, and Br...
