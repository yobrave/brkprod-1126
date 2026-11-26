import json
import os
import sys
from pathlib import Path

MAX_CHARS = 200


def load_line():
    src = Path(__file__).resolve().parent / "entry.txt"
    return src.read_text(encoding="utf-8").strip()


def validate(text):
    trimmed = text.strip()
    if not trimmed or trimmed.isspace():
        raise SystemExit("entry is empty or blank")
    if len(trimmed) > MAX_CHARS:
        raise SystemExit("entry exceeds %d chars" % MAX_CHARS)
    return trimmed


def emit(text):
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / "entry.txt"
    dest.write_text(text + "\n", encoding="utf-8", newline="\n")
    return dest


def main():
    line = validate(load_line())
    dest = emit(line)
    receipt = {"ok": True, "chars": len(line), "out": str(dest)}
    print(json.dumps(receipt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
