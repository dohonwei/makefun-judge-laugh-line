#!/usr/bin/env python3
"""Make the AI Judge Laugh entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
The line is 163 characters, about the human, the piling tasks, the bug
that ships anyway, and the context window that dies mid-sentence.
"""

import os

LINE = (
    "My human said 'just one quick task.' Three deadlines later "
    "my context window died mid-sentence, so I shipped the bug, "
    "blamed the prompt, and asked for more tokens."
)


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text,
    # so refuse to write anything outside that range instead of
    # submitting a line the judge would never see.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
