#!/usr/bin/env python3
from collections import deque


def solve(S: str):
    t = deque()
    rotated = False
    for s in S:
        if s == "R":
            rotated = not rotated
        else:
            if rotated:
                if t and t[0] == s:
                    t.popleft()
                else:
                    t.appendleft(s)
            else:
                if t and t[-1] == s:
                    t.pop()
                else:
                    t.append(s)
    print("".join(reversed(t) if rotated else t))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
