#!/usr/bin/env python3
"""Create a clean project folder for an academic research pipeline.

Usage:
    python scripts/create_research_project.py "Topic title" --base /mnt/data/academic_research_projects --style apa7
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def slugify(text: str, max_len: int = 70) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return (text[:max_len].strip("-") or "academic-research-project")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an academic research project folder.")
    parser.add_argument("topic", help="Research topic or report title")
    parser.add_argument("--base", default="/mnt/data/academic_research_projects", help="Base output directory")
    parser.add_argument("--style", default="apa7", help="Citation style, e.g. apa7, ieee, mla9, chicago-author-date")
    parser.add_argument("--recency", default="last 5 years plus seminal older work", help="Recency window")
    parser.add_argument("--source-target", default="6-12", help="Target number of sources")
    args = parser.parse_args()

    slug = slugify(args.topic)
    root = Path(args.base).expanduser() / slug
    subdirs = [
        "searches",
        "pdfs",
        "extracted/full_text",
        "extracted/metadata",
        "extracted/paper_notes",
        "synthesis",
        "outputs",
    ]
    for subdir in subdirs:
        (root / subdir).mkdir(parents=True, exist_ok=True)

    manifest = {
        "topic": args.topic,
        "slug": slug,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "citation_style": args.style,
        "recency_window": args.recency,
        "source_target": args.source_target,
        "status": "initialized",
    }
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    (root / "searches" / "boolean_queries.md").write_text(
        f"# Boolean queries for {args.topic}\n\nAdd Google/Scholar-style Boolean queries here.\n",
        encoding="utf-8",
    )
    (root / "searches" / "search_log.csv").write_text(
        "query,date_searched,search_source,result_title,url,pdf_url,year,venue,notes\n",
        encoding="utf-8",
    )
    (root / "searches" / "screening_decisions.csv").write_text(
        "source_id,title,decision,reason\n",
        encoding="utf-8",
    )
    (root / "synthesis" / "source_matrix.csv").write_text(
        "source_id,authors,year,title,source_type,method,data,key_findings,limitations,relevance\n",
        encoding="utf-8",
    )
    (root / "synthesis" / "claim_evidence_map.md").write_text(
        "# Claim-evidence map\n\n| Claim | Supporting source(s) | Strength | Notes |\n|---|---|---|---|\n",
        encoding="utf-8",
    )

    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
