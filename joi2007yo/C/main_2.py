print("".join(chr(((ord(ch) - ord("A")) - 3) % 26 + ord("A")) for ch in input()))
