#!/usr/bin/env python3

import sys

def main():
    N, Q = map(int, input().split())
    grid = [[0 for _ in range(N)] for _ in range(N)]
    rot = 0
    flipped = False  # rot == 0状態でみたときに左右反転している

    def _show():
        grid_1 = []
        for row in grid:
            grid_1.append(list(reversed(row)) if flipped else row)

        grid_2 = []
        if rot == 1:
            for w in range(N):
                row = []
                for h in range(N - 1, -1, -1):
                    row.append(grid_1[h][w])
                grid_2.append(row)
        elif rot == 2:
            for h in range(N - 1, -1, -1):
                row = []
                for w in range(N - 1, -1, -1):
                    row.append(grid_1[h][w])
                grid_2.append(row)
        elif rot == 3:
            for w in range(N - 1, -1, -1):
                row = []
                for h in range(N):
                    row.append(grid_1[h][w])
                grid_2.append(row)
        else:
            grid_2 = grid_1

        for row in grid_2:
            print("".join(str(e) for e in row))

    if Q == 0:  # for debugging
        queries = [line.rstrip().split() for line in sys.stdin.readlines()]
    else:
        queries = [[e for e in input().split()] for _ in range(Q)]
    for i, query in enumerate(queries, start=1):
        t = int(query[0])
        if t == 1:
            h, w = int(query[1]) - 1, int(query[2]) - 1
            if rot == 1:  # 90度
                h0 = N - 1 - w
                w0 = h
            elif rot == 2:
                h0 = N - 1 - h
                w0 = N - 1 - w
            elif rot == 3:
                h0 = w
                w0 = N - 1 - h
            else:
                h0, w0 = h, w
            if flipped:
                w0 = N - 1 - w0
            grid[h0][w0] = (grid[h0][w0] + 1) % 2
        elif t == 2:
            c = query[1]
            if c == "A":
                rot = (rot + 1) % 4
            else:
                rot = (rot + 3) % 4
        else:
            c = query[1]
            flipped = not flipped
            if rot in [0, 2]:
                if c == "A":
                    rot = (rot + 2) % 4
            else:
                if c == "B":
                    rot = (rot + 2) % 4
        if Q == 0:
            print(i, f"rot: {rot}, flipped: {flipped}, query: {query}")
            _show()

    if Q == 0:
        print()
    _show()


if __name__ == "__main__":
    main()
