"""Write the 24 November 2026 front-page image to the output directory.

Standard library only. Copies news.png (drawn by draw_news.py) next to
this file into MAKEFUN_OUTPUT_DIR (or /output) as entry.png, refusing
files over the competition's 1 MiB limit. Deterministic: the same input
bytes always produce the same output bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "news.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
OUT = os.path.join(OUT_DIR, "entry.png")
LIMIT = 1048576


def main():
    size = os.path.getsize(SRC)
    if size > LIMIT:
        print(f"news.png is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    if os.path.getsize(OUT) != size:
        print("copy size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {OUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
