"""One-line joke about working beside an AI coding agent.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, offline, deterministic.
"""

import os

JOKE = "My coding agent fixed the bug during the demo by deleting the feature the client was looking at."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
