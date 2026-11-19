#!/usr/bin/env python3
"""Entrypoint: copy the rendered front page to the output directory.

The page itself is drawn by draw.py (Pillow, stdlib + Pillow only).
This entrypoint uses only the standard library.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", HERE)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    if os.path.abspath(src) != os.path.abspath(dst):
        shutil.copyfile(src, dst)
    print("copied entry.png to", dst)


if __name__ == "__main__":
    sys.exit(main())
