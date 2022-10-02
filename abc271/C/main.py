#!/usr/bin/env python3
from collections import Counter


def solve(N: int, A: "List[int]"):
    counter = Counter(A)
    c = 0
    B = []
    for b in sorted(counter.keys()):
        B.append(b)
        rem = counter[b] - 1
        if rem > 0:
            c += rem
    i = 0
    ans = 0
    while i < len(B):
        b = B[i]
        if b == ans + 1:
            i += 1
            ans += 1
        elif c >= 2:
            c -= 2
            ans += 1
        elif b < ans + 1:
            i += 1
            c += 1
        else:
            B.pop()
            c += 1
    while c >= 2:
        ans += 1
        c -= 2
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
