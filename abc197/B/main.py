#!/usr/bin/env python3

DEBUG = False

def dprint(*args, **kwargs):
    if not DEBUG:
        return
    import sys
    args = ("#",) + args
    kwargs["file"] = sys.stderr
    print(*args, **kwargs)


def main():
    H, W, X, Y = [int(e) for e in input().split()]

    # - #, .
    table: "List[List[str]]" = []
    for h in range(H):
        table.append(list(input()))

    count = 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = X - 1, Y - 1
        while True:
            x, y = x + dx, y + dy
            if (
                    x < 0 or len(table) <= x or y < 0 or len(table[x]) <= y or table[x][y] == "#"
            ):
                break
            dprint(x, y, table[x][y])
            count += 1
    print(count)


if __name__ == "__main__":
    main()
