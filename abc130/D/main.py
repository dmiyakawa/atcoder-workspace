#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, K: int, A: "List[int]"):
    left, right, total = 0, 0, 0
    ans = 0
    while True:
        while total < K:
            if right == N:
                break
            total += A[right]
            right += 1
        while total >= K:
            ans += N - right + 1
            total -= A[left]
            left += 1
        if right == N:
            break
    print(ans)







def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)


if __name__ == "__main__":
    main()
