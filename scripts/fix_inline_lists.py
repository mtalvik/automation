#!/usr/bin/env python3
import re
from pathlib import Path


def split_inline_list(text: str) -> str:
    # Matches lines like: "Heading: - item a - item b - item c" or "**Heading:** - item a – item b"
    # Keeps the leading text up to ':' then converts following "- ..." chunks to bullet list items
    stripped = text.strip()
    m = re.match(
        r"^(?P<prefix>(\*\*[^\n:]{2,}\*\*|[^\n:]{2,})):\s*[–-]\s*(?P<rest>.+)$", stripped)
    if not m:
        return text

    prefix = m.group("prefix").strip()
    rest = m.group("rest").strip()

    # Split on ' - ' or ' – ' boundaries that separate list items
    # Use regex to avoid splitting inside code backticks
    parts = re.split(r"\s+[–-]\s+", rest)
    # Basic guard: need at least two items to warrant a list
    if len(parts) < 2:
        return text

    # Build new block: keep the prefix line as a bold label if it already looks like a heading-like lead
    # Keep the original prefix with trailing colon on its own line
    lines = [f"{prefix}:"]
    for p in parts:
        p = p.strip()
        if not p:
            continue
        lines.append(f"- {p}")
    return "\n".join(lines)


def transform_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    changed = False

    new_lines = []
    for line in lines:
        # Skip code blocks to avoid altering content inside fenced blocks
        new_lines.append(line)
    content = "\n".join(new_lines)

    # Process outside code blocks only: split by code fences and transform only even segments (non-code)
    segments = re.split(r"(^```.*?$|^~~~.*?$)", content, flags=re.MULTILINE)
    rebuilt = []
    in_code = False
    for seg in segments:
        if re.match(r"^```.*$|^~~~.*$", seg, flags=re.MULTILINE):
            in_code = not in_code
            rebuilt.append(seg)
            continue
        if in_code:
            rebuilt.append(seg)
            continue
        # Transform paragraph-wise: handle only single-line inline lists
        transformed = []
        for ln in seg.splitlines():
            new_ln = split_inline_list(ln)
            if new_ln != ln:
                changed = True
            transformed.append(new_ln)
        rebuilt.append("\n".join(transformed))

    new_content = "".join(rebuilt)
    if changed and new_content != original:
        path.write_text(new_content, encoding="utf-8")
    return changed


def main():
    root = Path(__file__).resolve().parents[1] / "docs"
    md_files = list(root.rglob("*.md"))
    total_changed = 0
    for f in md_files:
        if transform_file(f):
            total_changed += 1
    print(f"Updated files: {total_changed}")


if __name__ == "__main__":
    main()
