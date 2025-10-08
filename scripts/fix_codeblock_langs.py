#!/usr/bin/env python3
import re
from pathlib import Path

# Heuristics: default to bash for shell-like snippets; otherwise 'text'
SHELL_HINTS = (
    r"^\s*\$ ",
    r"\bapt(-get)?\b|\byum\b|\bdnf\b|\bpip(3)?\b|\bpython(3)?\b|\bmkdocs\b",
    r"\bdocker\b|\bkubectl\b|\bterraform\b|\bansible(-playbook)?\b|\bgit\b",
    r"^\s*# .*",
)
SHELL_REGEX = re.compile("|".join(SHELL_HINTS), re.IGNORECASE | re.MULTILINE)

CODE_BLOCK_OPEN = re.compile(r"^```\s*$")
CODE_BLOCK_LANG = re.compile(r"^```\s*([a-zA-Z0-9_+-]+)\s*$")


def guess_lang(block_text: str) -> str:
    if SHELL_REGEX.search(block_text):
        return "bash"
    # Simple JSON/YAML/HCL detectors
    if re.search(r"^{[\s\S]*}$", block_text.strip()):
        return "json"
    if re.search(r"(?m)^\s*([A-Za-z0-9_\-]+)\s*:\s*", block_text):
        return "yaml"
    if re.search(r"(?m)^\s*[a-zA-Z0-9_]+\s*=\s*\{", block_text):
        return "hcl"
    return "text"


def fix_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    fixed = []
    i = 0
    changed = 0
    while i < len(lines):
        line = lines[i]
        m_open_plain = CODE_BLOCK_OPEN.match(line)
        m_open_lang = CODE_BLOCK_LANG.match(line)
        if m_open_lang:
            # already has language
            fixed.append(line)
            i += 1
            continue
        if m_open_plain:
            # collect until closing fence
            start = i
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("```"):
                block.append(lines[i])
                i += 1
            # i is at closing fence or EOF
            lang = guess_lang("\n".join(block))
            fixed.append(f"```{lang}")
            fixed.extend(block)
            if i < len(lines):
                fixed.append(lines[i])  # closing fence
                i += 1
            changed += 1
            continue
        # normal line
        fixed.append(line)
        i += 1
    if changed:
        path.write_text("\n".join(fixed) + "\n", encoding="utf-8")
    return changed


def main():
    docs_dir = Path("docs")
    total = 0
    for md in docs_dir.rglob("*.md"):
        total += fix_file(md)
    print(f"Updated code block languages in {total} blocks")


if __name__ == "__main__":
    main()
