"""One Line, One Chill — a single sentence of horror.

This entry writes exactly one sentence to /output/entry.txt, and nothing
else. The sentence is a quiet, uncanny domestic detail: a child's
reflection that has started speaking a half-second early — and has now
stopped waiting for the child at all. The output is deterministic: the
same bytes on every run.
"""

ENTRY = "Since Tuesday, my son's reflection has been mouthing his words half a second before he says them, and this morning it stopped waiting for him."

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main():
    """Write the single horror sentence to /output/entry.txt."""
    import os

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
