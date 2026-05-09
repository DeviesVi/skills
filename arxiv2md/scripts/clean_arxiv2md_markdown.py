#!/usr/bin/env python3
"""Clean common arxiv2md/ar5iv Markdown artifacts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


MATH_ITALIC_CHARS = {
    "𝑎": "a",
    "𝑏": "b",
    "𝑐": "c",
    "𝑑": "d",
    "𝑒": "e",
    "𝑓": "f",
    "𝑔": "g",
    "ℎ": "h",
    "𝑖": "i",
    "𝑗": "j",
    "𝑘": "k",
    "𝑙": "l",
    "𝑚": "m",
    "𝑛": "n",
    "𝑜": "o",
    "𝑝": "p",
    "𝑞": "q",
    "𝑟": "r",
    "𝑠": "s",
    "𝑡": "t",
    "𝑢": "u",
    "𝑣": "v",
    "𝑤": "w",
    "𝑥": "x",
    "𝑦": "y",
    "𝑧": "z",
}


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join('"' + value.replace('"', '\\"') + '"' for value in values) + "]"


def clean_math_alt_text(md: str) -> str:
    """Remove common ar5iv visual math alt-text duplicated around simple formulas."""

    math_chars = "".join(MATH_ITALIC_CHARS)

    def simple_expr_repl(match: re.Match[str]) -> str:
        var, op, number, math_var = match.groups()
        if MATH_ITALIC_CHARS.get(math_var) != var:
            return match.group(0)
        return f"${var}{op}{number}$"

    # Examples:
    #   d + 1 𝑑 1 d+1 -> $d+1$
    #   d = 5 𝑑 5 d=5 -> $d=5$
    md = re.sub(
        rf"(?<![\w$])([a-z])\s*([+=\-])\s*(\d+)\s+([{math_chars}])\s+\d+\s+\1\s*\2\s*\3(?![\w$])",
        simple_expr_repl,
        md,
    )

    def simple_var_repl(match: re.Match[str]) -> str:
        var, math_var = match.groups()
        if MATH_ITALIC_CHARS.get(math_var) != var:
            return match.group(0)
        return f"${var}$"

    # Examples:
    #   v 𝑣 v -> $v$
    #   distance- d 𝑑 d code -> distance-$d$ code
    md = re.sub(
        rf"(?<![\w$])([a-z])\s+([{math_chars}])\s+\1(?![\w$])",
        simple_var_repl,
        md,
    )
    md = re.sub(r"(?<=\w)-\s+(\$[a-z]\$)", r"-\1", md)

    # A single displayed zero can become "0 0" in prose.
    md = re.sub(r"\bonly 0 0 or\b", r"only $0$ or", md)

    return md


def clean_latex_fragments(md: str) -> str:
    """Normalize LaTeX fragments that ar5iv emits but KaTeX often rejects."""

    delimiter_replacements = {
        r"\big{(}": r"\bigl(",
        r"\big{)}": r"\bigr)",
        r"\Big{(}": r"\Bigl(",
        r"\Big{)}": r"\Bigr)",
        r"\bigg{(}": r"\biggl(",
        r"\bigg{)}": r"\biggr)",
        r"\Bigg{(}": r"\Biggl(",
        r"\Bigg{)}": r"\Biggr)",
        r"\big{\{}": r"\bigl\{",
        r"\big{\}}": r"\bigr\}",
        r"\Big{\{}": r"\Bigl\{",
        r"\Big{\}}": r"\Bigr\}",
        r"\big{|}": r"\big|",
        r"\Big{|}": r"\Big|",
        r"\bigg{|}": r"\bigg|",
        r"\Bigg{|}": r"\Bigg|",
    }
    for old, new in delimiter_replacements.items():
        md = md.replace(old, new)
    return md


def clean_markdown(md: str, authors: list[str], affiliations: list[str]) -> str:
    if authors:
        replacement = f"authors: {yaml_list(authors)}"
        if affiliations:
            replacement += "\n" + f"affiliations: {yaml_list(affiliations)}"
        md = re.sub(r"^authors: \[[^\n]+\]$", replacement, md, flags=re.M)

    # The generated TOC often contains noisy ar5iv math alt-text; headings remain in the body.
    md = re.sub(r"\n## Contents\n[\s\S]*?(?=\n## Abstract\n)", "\n", md)
    md = re.sub(r"\n## Abstract\n\nAbstract\s+", "\n## Abstract\n\n", md)

    replacements = {"\u00a0": " "}
    for old, new in replacements.items():
        md = md.replace(old, new)
    md = clean_math_alt_text(md)
    md = clean_latex_fragments(md)

    md = re.sub(
        r"\[ \[\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*\] \] delimited-\[\]\s*[0-9 ]+\s*\[\\!\[\1,\2,\3\]\\!\]",
        r"$[\\![\1,\2,\3]\\!]$",
        md,
    )

    md = re.sub(
        r"^(#{1,6}\s+(?:Definition|Claim|Theorem|Lemma|Corollary|Proposition|Example|Result|Observation)\s+\d+)\s+\.$",
        r"\1",
        md,
        flags=re.M,
    )
    md = re.sub(r"^###### (Definition \d+)\n(?=######|\n#{2,3}|\Z)", "", md, flags=re.M)
    md = re.sub(r"^###### (Definition \d+)$", r"**\1**", md, flags=re.M)
    md = re.sub(r"^###### (Claim \d+)$", r"**\1**", md, flags=re.M)
    md = re.sub(r"^###### (Proof)\.$", r"**\1.**", md, flags=re.M)
    md = re.sub(r"^(#{3,6})#{3,6}\s+", r"\1 ", md, flags=re.M)

    def image_repl(match: re.Match[str]) -> str:
        caption = re.sub(r"\s+", " ", match.group(1)).strip()
        url = match.group(2).strip()
        alt = re.sub(r"[\[\]()`]", "", caption) or "Figure"
        if alt == "(a)":
            alt = "Figure"
        return f"\n![{alt}]({url})\n"

    md = re.sub(r"\nFigure: ([^\n]+)\nRefer to caption: (https://[^\s]+)\n", image_repl, md)

    def display_math_repl(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        number = match.group(2)
        return f"$$\n{body}\n\\tag{{{number}}}\n$$"

    md = re.sub(r"\$\$\s*\$\\displaystyle([\s\S]*?)\$\s*\((\d+)\)\s*\$\$", display_math_repl, md)
    md = re.sub(r"\$\$\s*\$([\s\S]*?)\$\s*\((\d+)\)\s*\$\$", display_math_repl, md)
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    return md


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--author", action="append", default=[], help="Correct author name; repeat as needed")
    parser.add_argument("--affiliation", action="append", default=[], help="Correct affiliation; repeat as needed")
    args = parser.parse_args()

    output = args.output or args.input.with_name(args.input.stem + ".cleaned" + args.input.suffix)
    md = args.input.read_text(encoding="utf-8")
    cleaned = clean_markdown(md, args.author, args.affiliation)
    output.write_text(cleaned, encoding="utf-8", newline="\n")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
