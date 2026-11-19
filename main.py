#!/usr/bin/env python3
"""Entrypoint: copy the front-page image to the grading output directory.

The repository ships entry.png (drawn by generate_image.py). This program
just places that same file at /output/entry.png, creating the directory
when it does not exist yet.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST = os.path.join(DEST_DIR, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("missing source image: " + SOURCE)
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    size = os.path.getsize(DEST)
    print("copied", SOURCE, "->", DEST, "(%d bytes)" % size)


if __name__ == "__main__":
    main()
