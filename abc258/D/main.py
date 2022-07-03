#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, X: int, A: "List[int]", B: "List[int]"):
    acc = [Inf for _ in range(N)]
    # ステージ i (0 <= i <= N - 1) までクリアしたあとでの再プレイの最短時間
    min_b = [Inf for _ in range(N)]
    for i, (a, b) in enumerate(zip(A, B)):
        if i == 0:
            min_b[i] = b
            acc[i] = a + b
        else:
            min_b[i] = min(min_b[i - 1], b)
            acc[i] = acc[i - 1] + a + b
    min_time = Inf
    # print(acc, min_b)
    # ステージ i まで一回クリアした時点で過去のステージを繰り返す
    for i in range(min(N, X)):
        min_time = min(acc[i] + min_b[i] * (X - i - 1), min_time)
    print(min_time)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, X, A, B)


if __name__ == "__main__":
    main()
