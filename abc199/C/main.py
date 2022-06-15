#!/usr/bin/env python3
from typing import List


def main():
    N = int(input())
    S: List[str] = list(input())
    Q = int(input())
    flipped = False
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            a = a - 1
            b = b - 1
            if flipped:
                a = (a + N) % (2 * N)
                b = (b + N) % (2 * N)
            S[a], S[b] = S[b], S[a]
        else:
            flipped = not flipped
    if flipped:
        S = S[N:] + S[:N]
    print("".join(S))


if __name__ == "__main__":
    main()
