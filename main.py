#!/usr/bin/env python3
"""news-image-20261120: copy the bundled front-page image to the output.

Reads the bundled ``news.jpg`` bytes and writes them unchanged to
``entry.png`` inside the output directory. The output directory is the
``MAKEFUN_OUTPUT_DIR`` environment variable when it is set, and
``/output`` when it is not.

Standard library only. No network, no randomness, no clock. Running the
program twice produces byte-identical output because it is a plain copy
of fixed bytes.
"""

import os
import pathlib
import sys


def main() -> int:
    source = pathlib.Path(__file__).resolve().parent / "news.jpg"
    if not source.is_file():
        print("error: bundled news.jpg is missing", file=sys.stderr)
        return 1
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    data = source.read_bytes()
    destination = output_dir / "entry.png"
    destination.write_bytes(data)
    # Deterministic confirmation line: the byte count depends only on
    # the bundled asset, never on the run.
    print(f"wrote {destination} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
