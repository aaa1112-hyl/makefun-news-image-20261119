#!/usr/bin/env python3
"""Entry for make.fun news-image-20261119.

Copies the front-page image (entry.png, drawn by generate_image.py in
this repository from Thursday 19 November 2026 world news) to
/output/entry.png. Standard library only, no network, deterministic.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
