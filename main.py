"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one original pickup line (max 200 characters) to
/output/entry.txt for the make.fun bounty
"One Line, One Minute: The Vending Machine Pickup Line Contest".

The line is built for the judge's brief, in the brief's own order:
1. Spoken by the machine itself, in the first person: it hums, it
   drops snacks, it names its own button (B7). No stranger in a bar
   could say this -- only a vending machine talks about dropping
   something from a coil when you press B7.
2. It lives in the machine's own world: its hum, its buttons, its
   coils' drop, its snacks. No generic talk about love.
3. The turn lands in the last few words: the machine offers its
   sweetest snack, then undercuts its own transaction -- exact
   change is optional, a smile will do, because the person is
   worth more than the snacks. The joke is the machine valuing
   the human above its own stock, and waiving its own price.
4. Short and speakable: one breath, one line, nothing tacked on
   after the punch.
5. Charming, not creepy: the machine is warm and a little shy --
   it has been humming for the person all day, it asks for nothing
   but a smile, and it compliments without leering or following.
"""

import os

LINE = "Hey \u2014 I\u2019ve been humming for you all day. Press B7 and I\u2019ll drop something sweet\u2026 exact change optional, a smile will do \u2014 you\u2019re worth more than my snacks."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # the gate refuses /output/entry.txt over 200 characters


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be blank"
    assert "\n" not in line, "line must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"line is {len(line)} characters, over the {MAX_CHARS} limit"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: prove the gate will see exactly the line, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line + "\n", "entry.txt does not match the line"


if __name__ == "__main__":
    main()
