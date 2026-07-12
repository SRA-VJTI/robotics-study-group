#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "lectures"
CACHE = ROOT / "tmp" / "pdfs" / "ocr"
OUTPUT = ROOT / "transcripts"

DECKS = [
    ("01", 44, "Introduction to Robot Learning", "week-01-introduction"),
    ("02", 46, "Robot Control and MDPs", "week-02-control-and-mdps"),
    ("03", 45, "Imitation Learning", "week-03-imitation-learning"),
    ("04", 45, "Reinforcement Learning I", "week-04-reinforcement-learning-i"),
    ("05", 36, "Reinforcement Learning II", "week-05-reinforcement-learning-ii"),
    ("06", 39, "Generative Models", "week-06-generative-models"),
    ("07", 39, "Sequence Modeling and Transformers", "week-07-sequence-modeling"),
    ("08", 55, "World Models", "week-08-world-models"),
    ("09", 59, "Generalist Robot Policies", "week-09-generalist-policies"),
    ("10", 57, "Embodied Reasoning and Test-time Scaling", "week-10-embodied-reasoning"),
    ("11", 50, "Frontiers and Open Problems", "week-11-frontiers"),
]


def normalize_ocr(raw: str) -> str:
    raw = raw.replace("\f", "").replace("\r\n", "\n").replace("\r", "\n")
    raw = raw.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")
    raw = raw.replace("\u2022", "-").replace("\u25aa", "-")

    lines: list[str] = []
    blank = False
    for original in raw.splitlines():
        line = re.sub(r"[ \t]+", " ", original).strip()
        if not line:
            if lines and not blank:
                lines.append("")
            blank = True
            continue

        blank = False
        line = line.replace("```", "'''")
        line = re.sub(
            r"(?i)\b(login|username|pwd|password)\s*[:=]\s*\S+",
            lambda match: f"{match.group(1)}: [REDACTED]",
            line,
        )
        lines.append(line)

    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) or "_No text was detected on this slide._"


def run_ocr(week: str, slide: int) -> tuple[str, int, str]:
    image = ASSETS / f"week-{week}" / f"slide-{slide}.jpg"
    cache_file = CACHE / f"week-{week}" / f"slide-{slide}.txt"
    cache_file.parent.mkdir(parents=True, exist_ok=True)

    if cache_file.exists():
        raw = cache_file.read_text(encoding="utf-8")
    else:
        result = subprocess.run(
            ["tesseract", str(image), "stdout", "-l", "eng", "--psm", "3"],
            check=True,
            capture_output=True,
            text=True,
        )
        raw = result.stdout
        cache_file.write_text(raw, encoding="utf-8")
    return week, slide, normalize_ocr(raw)


def write_transcript(
    week: str, count: int, title: str, slug: str, text_by_slide: dict[tuple[str, int], str]
) -> None:
    parts = [
        f"# Week {week} - {title}: OCR transcript",
        "",
        f"[← Course home](../README.md) · **Default OCR view** · "
        f"[Open optional slide gallery →](../curriculum/{slug}.md)",
        "",
        "> This is an automated OCR transcript generated from the locally rendered slide images. "
        "Use the image as the source of truth for equations, diagrams, citations, and small text.",
        "",
    ]

    for slide in range(1, count + 1):
        parts.extend(
            [
                f"## Slide {slide}",
                "",
                f"![{title} - slide {slide}](../assets/lectures/week-{week}/slide-{slide}.jpg)",
                "",
                "```text",
                text_by_slide[(week, slide)],
                "```",
                "",
            ]
        )

    parts.extend(
        [
            "---",
            "",
            f"[← Course home](../README.md) · "
            f"[Open optional slide gallery →](../curriculum/{slug}.md)",
        ]
    )
    (OUTPUT / f"{slug}.md").write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> None:
    if shutil.which("tesseract") is None:
        raise SystemExit("Tesseract is required. Install it before running this script.")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    jobs = [(week, slide) for week, count, _, _ in DECKS for slide in range(1, count + 1)]
    extracted: dict[tuple[str, int], str] = {}

    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(run_ocr, week, slide) for week, slide in jobs]
        for index, future in enumerate(as_completed(futures), start=1):
            week, slide, text = future.result()
            extracted[(week, slide)] = text
            if index % 50 == 0 or index == len(futures):
                print(f"OCR complete: {index}/{len(futures)} slides")

    for deck in DECKS:
        write_transcript(*deck, extracted)
    print(f"Wrote {len(DECKS)} Markdown transcripts to {OUTPUT}")


if __name__ == "__main__":
    main()
