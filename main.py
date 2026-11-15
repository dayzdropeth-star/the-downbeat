"""Entry for make.fun bounty agency-poem-01: "Write the best poem about agency".

Writes a single original poem to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, falling back to the current directory).

Pure standard library, no network, no randomness, no clock: two runs
write byte-identical output.
"""

import os

POEM = """The Downbeat

The baton rises, and nothing sounds.
That is the first lesson: the power
is not in the baton, but in the room
that answers it.

He plays no note. He never has.
The violins carry the line he chose;
the oboe enters on his nod; the brass
waits for the lift of his wrist. The silence
after is his too.

One night the cellos miss their cue.
He waits — a whole bar of nothing —
and learns the edge of what is his:
he can ask. He cannot take.
The music goes on without him.

At the last chord he lowers his arms.
The applause rises for the players,
and he bows, knowing the music was his
only because he gave it away.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
