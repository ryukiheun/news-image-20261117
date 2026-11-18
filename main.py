#!/usr/bin/env python3
"""Entry for make.fun news-image-20261117.

Copies the finished infographic (entry.png, held in this
repository) to the output path. Standard library only, no
network, and the copy is byte-identical on every run, so the
grader's two runs produce the same bytes.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    # Confirm the copy is complete: a partial write must not pass
    # silently, since the grader runs the program twice and both
    # runs must write the same bytes.
    if os.path.getsize(target) != os.path.getsize(source):
        print("error: copied file size differs from entry.png",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
