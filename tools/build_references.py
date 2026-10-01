#!/usr/bin/env python3
"""Build the bruin-expert skill references from a checkout of bruin-data/bruin.

Reads <src>/docs (VitePress markdown) and <src>/templates, converts the docs to
standalone markdown (no VitePress syntax, links rewritten to relative paths),
copies template sources, and writes per-category indexes.

Usage:
    python3 tools/build_references.py --src /path/to/bruin --out agents/skills/bruin-expert/references

Only needs the Python 3 standard library. The source checkout only has to
contain docs/ and templates/ (a sparse checkout is enough, see tools/sync.sh).
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import subprocess
import sys
from pathlib import Path

DOCS_BASE_URL = "https://getbruin.com/docs/bruin/"

# (id, title, path prefixes relative to docs/). Order matters: first match wins.
CATEGORIES = [
    ("core-concepts", "Core concepts and getting started", [
        "index.md", "overview.md", "core-concepts/",
        "getting-started/introduction/", "getting-started/tutorials/",
        "getting-started/concepts.md", "getting-started/design-principles.md",
        "getting-started/features.md", "getting-started/telemetry.md",
    ]),
    ("pipelines", "Pipelines", ["pipelines/", "getting-started/concurrency.md"]),
    ("assets", "Assets", ["assets/"]),
    ("variables", "Variables", ["variables/"]),
    ("connections-platforms", "Connections and platforms", [
        "connections/", "platforms/", "getting-started/lakehouse.md",
        "getting-started/credentials.md",
    ]),
    ("data-ingestion", "Data ingestion (ingestr sources, reverse ETL)", ["ingestion/"]),
    ("commands", "Commands (CLI reference)", ["commands/"]),
    ("data-governance", "Data governance (quality checks, glossary, policies)", [
        "quality/", "getting-started/glossary.md", "getting-started/policies.md",
    ]),
    ("deployment-cicd", "Deployment and CI/CD", ["deployment/", "cicd/"]),
    ("secret-providers", "Secret providers", ["secrets/"]),
    ("templates", "Templates", [
        "getting-started/templates.md", "getting-started/templates-docs/",
    ]),
    ("developer-tools", "Developer tools (VS Code extension, MCP, dev env)", [
        "vscode-extension/", "getting-started/bruin-mcp.md", "getting-started/devenv.md",
    ]),
    ("bruin-cloud", "Bruin Cloud", ["cloud/"]),
]

SKIP_DIR_NAMES = {"node_modules", ".vitepress", "public"}
BINARY_SUFFIXES = {
    ".csv", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".parquet", ".db",
    ".duckdb", ".sqlite", ".zip", ".gz", ".tar", ".pdf", ".xlsx", ".webp", ".mp4",
}
MAX_TEMPLATE_FILE_BYTES = 300_000
QUOTE_KINDS = {"tip", "warning", "info", "danger", "details", "note", "important", "caution"}

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
CONTAINER_RE = re.compile(r"^(\s*):::\s*([\w-]+)?\s*(.*?)\s*$")
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)((?:\s+\"[^\"]*\")?)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")
IMG_TAG_RE = re.compile(r"<img\b[^>]*?>", re.I)
BADGE_RE = re.compile(r"<Badge\b[^>]*?text=\"([^\"]*)\"[^>]*?/?>")
CODEVIEWER_RE = re.compile(r"<CodeViewer\b[^>]*?/>")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    try:
        return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    block = text[4:end]
    rest = text[end + 4:].lstrip("\n")
    meta: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip("'\"")
    return meta, rest


class Converter:
    def __init__(self, docs_root: Path):
        self.docs_root = docs_root

    def resolve_link(self, target: str, src_file: Path, out_file_rel: Path) -> str:
        if target.startswith(DOCS_BASE_URL):
            # Absolute link to the published docs: resolve it against the local copy.
            target = "/" + target[len(DOCS_BASE_URL):]
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            return target
        path, _, anchor = target.partition("#")
        anchor = f"#{anchor}" if anchor else ""
        if not path:
            return target
        base = self.docs_root if path.startswith("/") else src_file.parent
        raw = (base / path.lstrip("/")).resolve() if path.startswith("/") else (base / path).resolve()
        candidates = [raw]
        stem = raw
        if raw.suffix in (".html",):
            stem = raw.with_suffix("")
        candidates += [stem.with_suffix(".md") if stem.suffix == "" else stem, Path(str(stem) + ".md"),
                       stem / "index.md"]
        for cand in candidates:
            try:
                rel = cand.relative_to(self.docs_root.resolve())
            except ValueError:
                continue
            if cand.is_file() and cand.suffix == ".md":
                rel_link = Path(
                    _relpath(rel, out_file_rel.parent)
                ).as_posix()
                return rel_link + anchor
        # Not a markdown page we ship: point at the published site.
        try:
            rel = raw.relative_to(self.docs_root.resolve()).as_posix()
        except ValueError:
            return target
        if not Path(rel).suffix:
            rel += ".html"
        return DOCS_BASE_URL + rel + anchor

    def convert(self, src_file: Path, out_file_rel: Path) -> tuple[str, dict[str, str]]:
        text = src_file.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
        meta, body = parse_frontmatter(text)
        out: list[str] = []
        in_fence = False
        fence_marker = ""
        in_script = False
        stack: list[str] = []

        def quoted() -> bool:
            return any(k in QUOTE_KINDS for k in stack)

        for line in body.split("\n"):
            if in_script:
                if "</script>" in line or "</style>" in line:
                    in_script = False
                continue
            fm = FENCE_RE.match(line)
            if fm:
                marker = fm.group(1)
                if not in_fence:
                    in_fence, fence_marker = True, marker[0] * 3
                elif marker.startswith(fence_marker) and line.strip().strip(marker[0]) == "":
                    in_fence = False
                out.append(("> " + line) if quoted() else line)
                continue
            if in_fence:
                out.append(("> " + line) if quoted() else line)
                continue

            stripped = line.strip()
            if stripped.startswith(("<script", "<style")) and not (
                "</script>" in stripped or "</style>" in stripped
            ):
                in_script = True
                continue
            if stripped.startswith(("<script", "<style")):
                continue

            cm = CONTAINER_RE.match(line)
            if cm:
                kind, title = cm.group(2), cm.group(3)
                if kind:
                    stack.append(kind)
                    if kind in QUOTE_KINDS:
                        label = kind.capitalize()
                        head = f"**{label}: {title}**" if title else f"**{label}**"
                        out.append("> " + head)
                        out.append(">")
                    # code-group and unknown kinds: drop the marker, keep content
                elif stack:
                    stack.pop()
                continue

            line = CODEVIEWER_RE.sub("*(interactive file viewer omitted; see references/template-sources/)*", line)
            line = BADGE_RE.sub(lambda m: f" ({m.group(1)})", line)
            line = IMAGE_RE.sub(lambda m: f"*[image: {m.group(1)}]*" if m.group(1) else "*[image]*", line)
            line = IMG_TAG_RE.sub(lambda m: _img_tag_alt(m.group(0)), line)
            line = LINK_RE.sub(
                lambda m: f"[{m.group(1)}]({self.resolve_link(m.group(2), src_file, out_file_rel)}{m.group(3)})",
                line,
            )
            if quoted():
                line = "> " + line if line.strip() else ">"
            out.append(line)

        result = "\n".join(out)
        result = re.sub(r"\n{3,}", "\n\n", result).strip() + "\n"
        title = meta.get("title", "")
        if not re.search(r"^#\s+\S", result, re.M) and title:
            result = f"# {title}\n\n{result}"
        return result, meta


def _img_tag_alt(tag: str) -> str:
    m = re.search(r'alt="([^"]*)"', tag)
    return f"*[image: {m.group(1)}]*" if m and m.group(1) else "*[image]*"


def _relpath(target: Path, start: Path) -> str:
    import os
    return os.path.relpath(target.as_posix(), start.as_posix() or ".")


def category_for(rel: str) -> str | None:
    for cid, _title, prefixes in CATEGORIES:
        for p in prefixes:
            if rel == p or (p.endswith("/") and rel.startswith(p)):
                return cid
    return None


def first_title_and_blurb(md: str, meta: dict[str, str]) -> tuple[str, str]:
    title = ""
    m = re.search(r"^#\s+(.+?)\s*$", md, re.M)
    if m:
        title = m.group(1)
    blurb = meta.get("description", "")
    if not blurb:
        in_fence = False
        for line in md.splitlines():
            s = line.strip()
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence or not s or s.startswith(("#", ">", "|", "-", "*", "<", "!", "[!", "---")):
                continue
            blurb = s
            break
    blurb = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", blurb)
    blurb = re.sub(r"[`*_]", "", blurb)
    if len(blurb) > 170:
        blurb = blurb[:167].rstrip() + "..."
    return title, blurb


def build(src: Path, out: Path) -> None:
    docs = src / "docs"
    templates = src / "templates"
    if not docs.is_dir():
        sys.exit(f"error: {docs} not found. --src must be a Bruin checkout containing docs/.")

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    conv = Converter(docs)
    entries: dict[str, list[tuple[str, str, str]]] = {cid: [] for cid, _, _ in CATEGORIES}
    unmapped: list[str] = []
    count = 0

    for f in sorted(docs.rglob("*.md")):
        rel_path = f.relative_to(docs)
        if any(part in SKIP_DIR_NAMES for part in rel_path.parts):
            continue
        rel = rel_path.as_posix()
        text, meta = conv.convert(f, rel_path)
        dest = out / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        count += 1
        title, blurb = first_title_and_blurb(text, meta)
        cid = category_for(rel)
        if cid is None:
            unmapped.append(rel)
            continue
        entries[cid].append((rel, title or rel_path.stem, blurb))

    idx_dir = out / "_indexes"
    idx_dir.mkdir()
    cat_titles = {cid: title for cid, title, _ in CATEGORIES}

    for cid, items in entries.items():
        lines = [f"# Index: {cat_titles[cid]}", "",
                 f"{len(items)} pages. Paths are relative to references/.", ""]
        for rel, title, blurb in items:
            suffix = f": {blurb}" if blurb else ""
            lines.append(f"- `{rel}` | {title}{suffix}")
        (idx_dir / f"{cid}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Template sources (real, working pipelines)
    tcount = 0
    tmpl_lines = ["# Index: template sources (complete example pipelines)", "",
                  "Real asset and pipeline files from the Bruin templates. Use them as pattern references "
                  "when writing pipeline.yml, asset definitions, materialization, checks and .bruin.yml. "
                  "Paths are relative to references/template-sources/.", ""]
    if templates.is_dir():
        for tdir in sorted(p for p in templates.iterdir() if p.is_dir()):
            files: list[str] = []
            for f in sorted(tdir.rglob("*")):
                if not f.is_file():
                    continue
                rel_in = f.relative_to(tdir)
                if any(part in SKIP_DIR_NAMES or part in {".git", "__pycache__", "logs"} for part in rel_in.parts):
                    continue
                if f.suffix.lower() in BINARY_SUFFIXES or f.name in {".gitkeep", ".gitignore"}:
                    # Template .gitignore files are skipped on purpose: inside this skill they would
                    # make git ignore the example .bruin.yml files that the templates ship.
                    continue
                if rel_in.as_posix().lower() == "readme.md":
                    continue  # already shipped via docs/getting-started/templates-docs
                if f.stat().st_size > MAX_TEMPLATE_FILE_BYTES:
                    continue
                try:
                    content = f.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                dest = out / "template-sources" / tdir.name / rel_in
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding="utf-8")
                files.append(rel_in.as_posix())
                tcount += 1
            readme_doc = out / "getting-started" / "templates-docs" / f"{tdir.name}-README.md"
            blurb = ""
            if readme_doc.is_file():
                _t, blurb = first_title_and_blurb(readme_doc.read_text(encoding="utf-8"), {})
            tmpl_lines.append(f"## {tdir.name}")
            if blurb:
                tmpl_lines.append(blurb)
            if readme_doc.is_file():
                tmpl_lines.append(f"Docs: `getting-started/templates-docs/{tdir.name}-README.md`")
            tmpl_lines.append("")
            for rel_in in files:
                tmpl_lines.append(f"- `template-sources/{tdir.name}/{rel_in}`")
            tmpl_lines.append("")
    (idx_dir / "template-sources.md").write_text("\n".join(tmpl_lines) + "\n", encoding="utf-8")

    sha = run(["git", "rev-parse", "HEAD"], cwd=src)
    date = run(["git", "log", "-1", "--format=%cs"], cwd=src)
    (out / "SOURCE.md").write_text(
        "# Source of these references\n\n"
        f"- Upstream: https://github.com/bruin-data/bruin (docs/ and templates/)\n"
        f"- Commit: {sha or 'unknown'}\n"
        f"- Commit date: {date or 'unknown'}\n"
        f"- Generated: {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n"
        f"- Doc pages: {count}\n"
        f"- Template source files: {tcount}\n\n"
        "The docs track the latest Bruin CLI. If the installed CLI is older, confirm flags with "
        "`bruin <command> --help` before relying on a reference page.\n"
        "Regenerate with `tools/sync.sh`.\n",
        encoding="utf-8",
    )

    top = ["# Bruin references: index of indexes", "",
           "Open the index for the area you need, then open only the pages it points to.", ""]
    for cid, title, _ in CATEGORIES:
        top.append(f"- `_indexes/{cid}.md` | {title} ({len(entries[cid])} pages)")
    top.append(f"- `_indexes/template-sources.md` | Complete template pipelines ({tcount} files)")
    top += ["", "See `SOURCE.md` for the upstream commit these were generated from.", ""]
    (out / "INDEX.md").write_text("\n".join(top), encoding="utf-8")

    print(f"docs pages written:       {count}")
    print(f"template source files:    {tcount}")
    for cid, title, _ in CATEGORIES:
        print(f"  {cid:24s} {len(entries[cid])}")
    if unmapped:
        print("\nWARNING: pages not mapped to any category (add them to CATEGORIES):", file=sys.stderr)
        for u in unmapped:
            print(f"  {u}", file=sys.stderr)
        sys.exit(2)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, type=Path, help="Path to a Bruin checkout (needs docs/ and templates/)")
    ap.add_argument("--out", required=True, type=Path, help="Output references/ directory")
    args = ap.parse_args()
    build(args.src.resolve(), args.out.resolve())


if __name__ == "__main__":
    main()
