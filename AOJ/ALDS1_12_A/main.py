#!/usr/bin/env python3

Inf = float("Inf")


def solve_with_prim(N, grid):
    min_costs = [Inf for _ in range(N)]
    used = [False for _ in range(N)]
    total = 0
    min_costs[0] = 0
    while True:
        v = -1
        for u in range(N):
            if not used[u] and (v == -1 or min_costs[u] < min_costs[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        total += min_costs[v]
        for u in range(N):
            if grid[v][u] != -1:
                min_costs[u] = min(min_costs[u], grid[v][u])
    print(total)


def main():
    N = int(input())
    grid = [[int(e) for e in input().split()] for _ in range(N)]
    solve_with_prim(N, grid)


if __name__ == "__main__":
    main()
