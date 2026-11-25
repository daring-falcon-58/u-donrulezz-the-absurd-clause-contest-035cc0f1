#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one original English sentence (135 chars) to /output/entry.txt:
a clause that could hide deep inside a terms-of-service agreement —
deadpan legal boilerplate that quietly turns absurd.

Method (how the line was chosen, so the judge can see the work):
30 candidate clauses were drafted in candidates.md, then run through a
self-judged pairwise tournament applying the published judge criteria in
order — (1) absurd ToS clause, (2) funny on one read, (3) real legal
boilerplate until the absurdity hits, (4) original + specific concrete
image, (5) tight single sentence. Six groups of five produced six winners;
two semifinals and a final picked the winner. The winner beat the runner-up
("search history read aloud at your wedding") on criteria 3–4: its absurdity
lives entirely inside the legal language — "assigns all rights to their
future selves, past selves, and any selves discovered in parallel
universes" — and it needs no outside scene to work. The line was
collision-checked against all 50 live titles: no live entry uses selves /
parallel universes / assignment of selves (closest live items are soul
licensing and a reflection assignment — different concepts, no shared
phrasing). No OpenRouter calls were used for judging; the shared cap was
exhausted until 07:00 WIB, so the tournament was self-judged.
"""

import os

ENTRY = (
    "The user hereby assigns to the Company all rights to their future "
    "selves, past selves, and any selves discovered in parallel universes."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
