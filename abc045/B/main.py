#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(S_A: str, S_B: str, S_C: str):
    ai = 0
    bi = 0
    ci = 0
    t = "a"
    while True:
        if t == "a":
            if ai >= len(S_A):
                break
            t = S_A[ai]
            ai += 1
        elif t == "b":
            if bi >= len(S_B):
                break
            t = S_B[bi]
            bi += 1
        else:
            if ci >= len(S_C):
                break
            t = S_C[ci]
            ci += 1
    print(t.upper())


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S_A = next(tokens)  # type: str
    S_B = next(tokens)  # type: str
    S_C = next(tokens)  # type: str
    solve(S_A, S_B, S_C)


if __name__ == "__main__":
    main()
