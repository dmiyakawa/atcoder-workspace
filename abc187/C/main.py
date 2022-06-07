#!/usr/bin/env python3


def main():
    N = int(input())
    cands = {}
    t = None
    for _ in range(N):
        s = input()
        if s[0] == "!":
            c = 1
            s = s[1:]
        else:
            c = 0
        if s in cands:
            if cands[s] != c:
                t = s
                break
        else:
            cands[s] = c
    print(t if t else "satisfiable")


if __name__ == "__main__":
    main()
