#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    A.sort(reverse=True)
    remaining_k = K
    for i in range(N):
        a = A[i]
        if remaining_k == 0:
            continue
        num_used_k = min(a // X, remaining_k)
        remaining_k -= num_used_k
        if a - num_used_k * X >= 0:
            A[i] = a - num_used_k * X

    A.sort()
    while remaining_k > 0 and A:
        popped = A.pop()
        if popped > 0:
            remaining_k -= 1
    print(sum(A))


if __name__ == "__main__":
    main()
