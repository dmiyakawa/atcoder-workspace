#!/usr/bin/env python3



def main():
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())
    # UDLR
    G = [[ch for ch in input().rstrip()] for _ in range(H)]
    i, j = 0, 0
    visited = set()
    while True:
        if (i, j) in visited:
            print(-1)
            return
        visited.add((i, j))
        op = G[i][j]
        if op == "U":
            ni, nj = i - 1, j
        elif op == "L":
            ni, nj = i, j - 1
        elif op == "R":
            ni, nj = i, j + 1
        else:
            ni, nj = i + 1, j
        if not (0 <= ni < H and 0 <= nj < W):
            print(i + 1, j + 1)
            break
        i, j = ni, nj


if __name__ == "__main__":
    main()
