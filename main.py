"""Entry point for the news-image-20261124 submission.

The front page is rendered ahead of time by render_frontpage.py and kept
in this repository as news.png. This program copies it to the path the
competition harness reads, /output/entry.png.
"""

import os
import shutil
import sys


def entry_image_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "news.png")


def main():
    source = entry_image_path()
    if not os.path.isfile(source):
        print("missing image: " + source, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    target = os.path.join("/output", "entry.png")
    shutil.copyfile(source, target)
    size = os.path.getsize(target)
    if size > 1024 * 1024:
        print("image over the 1 MiB cap: " + str(size) + " bytes",
              file=sys.stderr)
        return 1
    print("wrote " + target + " (" + str(size) + " bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
