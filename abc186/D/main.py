#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, A: "List[int]"):
    A.sort(reverse=True)
    ans = 0
    B = [a for a in A]
    for i in range(1, N):
        B[i] += B[i - 1]

    for i in range(N - 1):
        s = B[N - 1] - B[i]
        ans += A[i] * (N - 1 - i) - s
    print(ans)



def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
