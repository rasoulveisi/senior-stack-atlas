#!/usr/bin/env python3
"""Assemble index.html from the parts in src/parts. Run from anywhere: python3 src/build.py"""
import pathlib

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
PARTS = SRC / "parts"

# (module id, sidebar label, chapter files in order)
MODULES = [
    ("express", "Module I · Express 5", ["11-express-a.html", "12-express-b.html"]),
    ("dotnet", "Module II · .NET 10", ["21-dotnet-a.html", "22-dotnet-b.html"]),
    ("react", "Module III · React + Next", ["31-react-a.html", "32-react-b.html"]),
]


def read(name):
    return (PARTS / name).read_text()


def module(key, label, files):
    chapters = "".join(read(f) for f in files)
    return (
        f'\n<section id="module-{key}" data-toc-group="{label}" class="scroll-mt-16">\n'
        + read(f"{key}-banner.html")
        + '<div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-10">\n'
        + chapters
        + "</div>\n</section>\n"
    )


html = read("_head.html") + read("00-overview.html")
html += "".join(module(*m) for m in MODULES)
html += read("_foot.html")

chapters = "".join(read(f) for m in MODULES for f in m[2])
answers = chapters.count("Interview answer") + chapters.count("Say it like a senior")
html = html.replace("data-count-qa>50+<", f"data-count-qa>{answers}<")

(ROOT / "index.html").write_text(html)
print(f"index.html written: {len(html) // 1024} KB, {answers} interview answers")
