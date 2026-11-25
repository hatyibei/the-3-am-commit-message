"""Entry for The 3 AM Commit Message: writes the commit message to /output/entry.txt."""

import os

TEXT = "fix: it works. I don't know why, I don't want to know why. Nobody touch this file. If it breaks, this commit was written by a ghost at 3 AM."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
