#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(H: int, W: int, N: int, a: "List[int]"):
    ai = 0
    h = 0
    w = 0
    ans = [[0 for _ in range(W)] for _ in range(H)]
    while h < H:
        ans[h][w] = ai + 1
        a[ai] -= 1
        if a[ai] == 0:
            ai += 1
        if h % 2 == 0:
            if w < W - 1:
                w += 1
            else:
                h += 1
        else:
            if w > 0:
                w -= 1
            else:
                h += 1
    print("\n".join(" ".join(str(n) for n in lst) for lst in ans))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(H, W, N, a)


if __name__ == "__main__":
    main()
