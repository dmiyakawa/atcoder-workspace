#!/usr/bin/env python3

Inf = float("inf")

def main():
    N = int(input())
    A = [[int(e) for e in input().split()] for _ in range(N)]
    cost = [[Inf for _ in range(N)] for _ in range(2**N)]
    for n in range(2**N - 1, 1, -1):
        for i in range(N):
            m = 1 << i
            if not (m & n):
                continue
            if n == 2**N - 1:
                cost[n][i] = A[i][0]
                continue
            min_c = Inf
            for j in range(N):
                l = 1 << j
                if l & n:
                    continue
                print(format(n, "b").zfill(N), i, j, format(n | l, "b"),
                      A[i][j], cost[n | l][j], A[i][j] + cost[n | l][j])
                min_c = min(min_c, A[i][j] + cost[n | l][j])
            cost[n][i] = min_c
    print(cost)
    print(cost[1][0])


if __name__ == "__main__":
    main()
