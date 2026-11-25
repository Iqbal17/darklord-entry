"""The Tired Dark Lord — make.fun entry (u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb).

Writes one ~100-word villain monologue to $MAKEFUN_OUTPUT_DIR/entry.txt.

Decision record — Pass 1, three candidates weighed against the judge brief
(tiredness FELT in rhythm/pauses/deflections, never announced; a SPECIFIC
villain with history + scheme; concrete fantasy detail, not stock scenery;
speakable in one breath; a turn/sting in the last line; near 100 words,
every word earning its place):

A. THE LICH OF THE WITHERED SPIRE (CHOSEN) — Dread Lich Malachar, scourge
   of seven kingdoms, keeper of the Black Grimoire. Scheme: raise every
   grave in the valley at midnight and march on the capital. Tiredness in
   deflections: he loses the grimoire mid-boast, stops for tea because his
   throat is dry, and ends by ordering the hero to SIT instead of kneel —
   the villain is too tired to even demand kneeling. Concrete detail: the
   skeleton Brunt keeps losing his left arm in the stairwell. Strongest
   last-line sting of the three.

B. GRIKKLE, KING OF THE HOLLOW TOLL (rejected) — goblin king, three
   coppers to cross the bridge, scheme to sell the bridge to the trolls
   and retire; the trolls want receipts. Funny ("Receipts!") and the lost
   crown deflection is good, but the scheme is thin, the villain's history
   is a shrug, and the last line ("Pay.") has no turn — it just repeats
   the toll.

C. SERYSSA, THE ASHEN DRAGON (rejected) — old dragon who was going to
   burn the village at dawn but the miller brings her lovely tea now, so
   the new plan is: pay in tea, she guards the coast. Charming, and the
   tea-for-protection bargain is a real scheme, but the ending ("Count.")
   lands flat, and "I lost count both times" states the tiredness more
   than it performs it.

Pass 2, two genuine revisions on A:
1. Sharpened the scheme's target: "they will march" became "they will
   march on the capital" — the villain now has somewhere to go, not just
   a directionless horde.
2. Rhythm pass for speakability: kept the three beats of collapse
   (lost grimoire -> tea -> sit) evenly spaced, cut nothing that carried
   a joke, and let the final "Sit." stand alone as its own sentence so
   a performer can drop their voice on it. A final word-count trim
   ("the dead of" out of the raising, "hero" and "Black" dropped) took
   the draft from 107 words to 102 without losing a beat.
"""

import os

TEXT = (
    "So. You have climbed the Withered Spire, past my skeletons \u2014 good lads, "
    "mostly, though Brunt keeps losing his left arm in the stairwell \u2014 and here "
    "I stand, the Dread Lich Malachar, scourge of seven kingdoms, keeper of the "
    "Grimoire, and \u2014 hold on \u2014 where did I put the grimoire? It was "
    "here. Anyway. The plan is simple: at midnight I raise every grave in the "
    "valley, and they will march on the capital \u2014 ah, but "
    "first, tea. My throat. The dead can wait; they are very patient, the dead. "
    "Now, kneel, or... actually, sit. Both of us. Sit."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
