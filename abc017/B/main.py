#!/usr/bin/env python3

def main():
    s = input()
    is_choku = True
    while s:
        if s.startswith("ch"):
            s = s[2:]
        elif s[0] in "oku":
            s = s[1:]
        else:
            is_choku = False
            break
    print("YES" if is_choku else "NO")


if __name__ == "__main__":
    main()
