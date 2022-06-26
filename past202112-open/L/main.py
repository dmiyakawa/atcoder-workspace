#!/usr/bin/env python3
# 解答確認後

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, P: int, A: "List[int]"):
    import bisect
    B = []
    for i, a in enumerate(reversed(A)):
        # 例えば2位がP点を主張するのは変だし
        # ビリから数えて2番目が0点を主張するのもおかしい
        if 0 <= a - i <= P - N + 1:
            B.append(a - i)
    C = []
    for b in B:
        i = bisect.bisect_right(C, b)
        if i >= len(C):
            C.append(b)
        else:
            C[i] = b
    print(N - len(C))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, A)


if __name__ == "__main__":
    main()
