"""The Funniest AI Excuse — writes one one-line excuse to /output/entry.txt.

The joke: the agent dodges blame by outsourcing the task to Future Me,
who ghosted it — a fresh, specific excuse in the agent's own voice.
"""

import os

LINE = "I outsourced your task to a future version of me, and he just left me on read \u2014 so the failure is technically scheduled."

assert LINE.strip(), "entry must not be blank"
assert "\n" not in LINE, "entry must be a single line"
assert len(LINE) <= 200, f"entry is {len(LINE)} chars, over the 200-char limit"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)}-char entry to /output/entry.txt")
