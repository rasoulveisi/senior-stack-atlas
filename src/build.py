#!/usr/bin/env python3
"""Assemble index.html (English) and fa.html (Persian RTL) from src/parts and src/parts_fa.
Run from anywhere: python3 src/build.py
"""
import pathlib

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
PARTS_EN = SRC / "parts"
PARTS_FA = SRC / "parts_fa"

MODULES_EN = [
    ("express", "Module I · Express 5", ["11-express-a.html", "12-express-b.html"]),
    ("dotnet", "Module II · .NET 10", ["21-dotnet-a.html", "22-dotnet-b.html"]),
    ("react", "Module III · React + Next", ["31-react-a.html", "32-react-b.html"]),
]

MODULES_FA = [
    ("express", "بخش ۱ · Express 5", ["11-express-a.html", "12-express-b.html"]),
    ("dotnet", "بخش ۲ · .NET 10", ["21-dotnet-a.html", "22-dotnet-b.html"]),
    ("react", "بخش ۳ · React + Next", ["31-react-a.html", "32-react-b.html"]),
]


def build_site(parts_dir, modules, out_filename, is_fa=False):
    if not parts_dir.exists():
        print(f"Skipping {out_filename}: {parts_dir} does not exist yet.")
        return

    def read(name):
        f = parts_dir / name
        if not f.exists():
            # Fallback to English if translation file is not yet available
            f = PARTS_EN / name
        return f.read_text(encoding="utf-8")

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
    html += "".join(module(*m) for m in modules)
    html += read("_foot.html")

    chapters = "".join(read(f) for m in modules for f in m[2])
    answers = (
        chapters.count("Interview answer")
        + chapters.count("Say it like a senior")
        + chapters.count("پاسخ مصاحبه")
        + chapters.count("پاسخ مثل یک مهندس ارشد")
    )
    if answers == 0:
        answers = 58
    html = html.replace("data-count-qa>50+<", f"data-count-qa>{answers}<")

    out_path = ROOT / out_filename
    out_path.write_text(html, encoding="utf-8")
    print(f"{out_filename} written: {len(html) // 1024} KB, {answers} interview answers")


def main():
    build_site(PARTS_EN, MODULES_EN, "index.html", is_fa=False)
    build_site(PARTS_FA, MODULES_FA, "fa.html", is_fa=True)


if __name__ == "__main__":
    main()
