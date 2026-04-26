#!/usr/bin/env python3
"""Extract text and basic metadata from PDFs in a research project folder.

Usage:
    python scripts/extract_pdfs.py /mnt/data/academic_research_projects/<project_slug>

The script tries PyMuPDF first, then pypdf. Install one of them if needed:
    python -m pip install pymupdf pypdf
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def clean_filename(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text)
    return text.strip("_") or "paper"


def extract_with_pymupdf(pdf_path: Path) -> tuple[str, dict]:
    import fitz  # type: ignore

    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text") or ""
        pages.append(f"\n\n--- PAGE {i} ---\n{text}")
    metadata = dict(doc.metadata or {})
    metadata["page_count"] = doc.page_count
    return "".join(pages).strip(), metadata


def extract_with_pypdf(pdf_path: Path) -> tuple[str, dict]:
    from pypdf import PdfReader  # type: ignore

    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append(f"\n\n--- PAGE {i} ---\n{text}")
    metadata = {str(k).lstrip("/"): str(v) for k, v in (reader.metadata or {}).items()}
    metadata["page_count"] = len(reader.pages)
    return "".join(pages).strip(), metadata


def extract_pdf(pdf_path: Path) -> tuple[str, dict, str]:
    try:
        text, metadata = extract_with_pymupdf(pdf_path)
        return text, metadata, "pymupdf"
    except Exception as first_error:
        try:
            text, metadata = extract_with_pypdf(pdf_path)
            return text, metadata, "pypdf"
        except Exception as second_error:
            raise RuntimeError(
                f"Could not extract {pdf_path.name}. PyMuPDF error: {first_error}; pypdf error: {second_error}"
            ) from second_error


def make_note_template(source_id: str, pdf_path: Path, metadata: dict, extractor: str) -> str:
    title = metadata.get("title") or pdf_path.stem.replace("_", " ")
    author = metadata.get("author") or ""
    return f"""# {source_id} - {title}

## Bibliographic metadata
- authors: {author}
- year:
- title: {title}
- venue:
- doi/url:
- source type:
- access status: full-pdf parsed
- local pdf: {pdf_path.name}
- extractor: {extractor}

## Research purpose

## Data and methods

## Key findings
- 

## Limitations stated by authors
- 

## Relevance to user topic

## Safe citation claims
- Claim:
  Evidence:
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from all PDFs in a research project folder.")
    parser.add_argument("project_dir", help="Project directory containing a pdfs/ folder")
    args = parser.parse_args()

    root = Path(args.project_dir).expanduser()
    pdf_dir = root / "pdfs"
    text_dir = root / "extracted" / "full_text"
    meta_dir = root / "extracted" / "metadata"
    notes_dir = root / "extracted" / "paper_notes"
    for directory in [text_dir, meta_dir, notes_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {pdf_dir}")
        return 0

    report = []
    for index, pdf_path in enumerate(pdfs, start=1):
        source_id = f"S{index:02d}"
        try:
            text, metadata, extractor = extract_pdf(pdf_path)
            metadata.update({
                "source_id": source_id,
                "local_pdf": pdf_path.name,
                "extracted_at_utc": datetime.now(timezone.utc).isoformat(),
                "extractor": extractor,
                "text_characters": len(text),
            })
            safe_stem = clean_filename(pdf_path.stem)
            (text_dir / f"{source_id}_{safe_stem}.txt").write_text(text, encoding="utf-8", errors="replace")
            (meta_dir / f"{source_id}_{safe_stem}.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
            note_path = notes_dir / f"{source_id}_{safe_stem}.md"
            if not note_path.exists():
                note_path.write_text(make_note_template(source_id, pdf_path, metadata, extractor), encoding="utf-8")
            report.append({"source_id": source_id, "pdf": pdf_path.name, "status": "ok", "characters": len(text)})
        except Exception as error:
            report.append({"source_id": source_id, "pdf": pdf_path.name, "status": "error", "error": str(error)})

    (root / "extracted" / "extraction_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
