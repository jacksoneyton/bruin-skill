# bruin-skill

Agent skills for working with [Bruin](https://github.com/bruin-data/bruin). Two parts:

1. The skills that `bruin ai skills all` installs (pipeline diagnosis, schema drift, freshness, duplicates, quality checks, maintenance actions, semantic layer).
2. `bruin-expert`, an added skill that carries the full Bruin documentation and the template pipelines as local references, so an agent can plan pipelines and assets correctly instead of guessing syntax.

## Install

Option A, from a machine with the Bruin CLI (installs part 1 only):

```
bruin ai skills all
```

Option B, from this repo (installs everything, no Bruin CLI needed):

The `agents` folder in this repo is `.agents` once installed. Use the install script, which works whether or not the project already has a `.agents` folder (for example after `bruin ai skills all`):

Linux or macOS:

```
git clone https://github.com/jacksoneyton/bruin-skill
bruin-skill/tools/install.sh <your-project>
```

Windows PowerShell:

```
git clone https://github.com/jacksoneyton/bruin-skill
.\bruin-skill\tools\install.ps1 -Project <your-project>
```

To copy by hand, copy the contents of `agents`, not the folder itself. A plain `cp -r agents <your-project>/.agents` nests the skills under `.agents/agents/` when `.agents` already exists.

```
mkdir -p <your-project>/.agents
cp -r bruin-skill/agents/. <your-project>/.agents/
```

The install copies overwrite files with the same path, so the upstream skills in `.agents/skills` are replaced by the copies in this repo. They match unless your Bruin CLI is newer. To add only the new skill, copy `agents/skills/bruin-expert` into `.agents/skills/`.

Some agents also read `.claude/skills/`. Bruin's own installer keeps `.claude` as a symlink to `.agents`. If your agent does not read `.agents/skills/`, point its skills folder at the same directory.

## What `bruin-expert` contains

```
agents/skills/bruin-expert/
  SKILL.md              routing table, core model, planning workflow, guardrails
  references/
    INDEX.md            index of indexes
    _indexes/           one index per category, with a summary line per page
    <docs tree>/        every page of the Bruin docs as standalone markdown
    template-sources/   real asset, pipeline, and config files from each Bruin template
    SOURCE.md           upstream commit and generation date
```

Categories covered: core concepts, pipelines, assets, variables, connections and platforms, data ingestion, commands, data governance, deployment and CI/CD, secret providers, templates, developer tools, Bruin Cloud.

## Refreshing the references

The references are generated, not hand-edited. To update them to the latest upstream docs:

```
tools/sync.sh          # Linux or macOS
tools/sync.ps1         # Windows PowerShell
```

Needs git and Python 3. It does a sparse clone of `docs/` and `templates/` from `bruin-data/bruin` (a few MB), converts the VitePress markdown to plain markdown, rewrites internal links to relative paths, and regenerates the indexes. To use an existing clone instead of fetching, set `BRUIN_SRC` to its path.

Commit the regenerated `references/` folder so other machines get it with a `git pull`.

## Notes

- The docs track the latest Bruin release. If the installed CLI is older, `bruin <command> --help` wins over a reference page.
- The upstream skills under `agents/skills/` other than `bruin-expert` are copies of what the Bruin CLI ships. Running `bruin ai skills all` overwrites them with the installed CLI's version.
