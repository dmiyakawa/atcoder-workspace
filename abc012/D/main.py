#!/usr/bin/env python3

Inf = float("inf")

def main():
    N, M = map(int, input().split())
    grid = [[(0 if i == j else Inf) for i in range(N)] for j in range(N)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        a -= 1
        b -= 1
        grid[a][b] = t
        grid[b][a] = t
    for k in range(N):
        for i in range(N):
            for j in range(N):
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
    print(min(max(grid[i]) for i in range(N)))

if __name__ == "__main__":
    main()
