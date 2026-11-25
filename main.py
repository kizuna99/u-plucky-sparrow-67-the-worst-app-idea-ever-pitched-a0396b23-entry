# SPDX-License-Identifier: MIT
"""Write the winning worst-app pitch to /output/entry.txt.

Passw0rdPal: a security app for the truly cautious whose protection
makes it unusable — typing your password correctly is treated as
proof the password was too guessable, so it changes it every time.
"""
import os

LINE = "Meet Passw0rdPal, the security app for the truly cautious that changes your password every time you type it correctly, because if you knew it, it was already too guessable."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
