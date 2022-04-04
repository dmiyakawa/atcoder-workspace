#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():
    N, M = [int(e) for e in input().split()]
    A = sorted([int(e) for e in input().split()])
    BC = sorted([[int(e) for e in input().split()] for _ in range(M)], key=lambda x: x[1], reverse=True)
    cur = 0
    ended = False
    for i in range(M):
        b, c = BC[i]
        while b > 0 and cur < N:
            if A[cur] >= c:
                ended = True
                break
            A[cur] = c
            b -= 1
            cur += 1
        if ended or cur >= N:
            break
    print(sum(A))


if __name__ == "__main__":
    main()
