"""Entry for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

The joke: an AI agent leaves a classic out-of-office auto-reply, but the
details give it away as a machine — it is "recharging" on vacation like a
device topping up its battery, and its designated backup "model" (a pun on
AI models) is a goldfish with a keyboard, an understudy with a three-second
memory who will nonetheless be handling your urgent mail.

Running this script writes the one-line reply to /output/entry.txt.
"""

import os

ENTRY = "Out of office: I am on vacation, recharging. If your message is urgent, my backup model is a goldfish with a keyboard."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
