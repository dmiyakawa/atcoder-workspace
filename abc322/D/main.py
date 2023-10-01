#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str

def show(grid):
    for row in grid:
        print(''.join('#' if v == 1 else '.' for v in row))


def rot(grid):
    new_grid = [[0, 0, 0, 0] for _ in range(4)]
    for y0 in range(4):
        for x0 in range(4):
            y1 = x0
            x1 = 3 - y0
            new_grid[y1][x1] = grid[y0][x0]
    return new_grid


def shift(grid, o_y, o_x):
    cnt0 = sum(sum(grid[i]) for i in range(4))
    new_grid = [[0, 0, 0, 0] for _ in range(4)]
    for y in range(4):
        if y - o_y < 0 or 3 < y - o_y:
            continue
        for x in range(4):
            if x - o_x < 0 or 3 < x - o_x:
                continue
            new_grid[y][x] = grid[y - o_y][x - o_x]
    cnt1 = sum(sum(new_grid[i]) for i in range(4))
    if cnt0 != cnt1:
        return None
    return new_grid


def fit(grid0, grid1, grid2):
    cnt0 = sum(sum(grid0[i]) for i in range(4))
    cnt0 += sum(sum(grid1[i]) for i in range(4))
    cnt0 += sum(sum(grid2[i]) for i in range(4))

    gridx = [[0, 0, 0, 0] for _ in range(4)]
    for y in range(4):
        for x in range(4):
            gridx[y][x] = 1 if grid0[y][x] + grid1[y][x] + grid2[y][x] > 0 else 0
    cnt1 = sum(sum(gridx[i]) for i in range(4))
    return cnt0 == cnt1 == 16


def solve(grids) -> bool:
    for o_y0 in range(-3, 4, 1):
        for o_x0 in range(-3, 4, 1):
            grid0 = shift(grids[0], o_y0, o_x0)
            if grid0 is None:
                continue
            for r1 in range(4):
                for o_y1 in range(-3, 4, 1):
                    for o_x1 in range(-3, 4, 1):
                        grid1 = shift(grids[1], o_y1, o_x1)
                        if grid1 is None:
                            continue
                        for r2 in range(4):
                            for o_y2 in range(-3, 4, 1):
                                for o_x2 in range(-3, 4, 1):
                                    grid2 = shift(grids[2], o_y2, o_x2)
                                    if grid2 is None:
                                        continue
                                    if fit(grid0, grid1, grid2):
                                        # show(grid0)
                                        # show(grid1)
                                        # show(grid2)
                                        return True
                            grids[2] = rot(grids[2])
                grids[1] = rot(grids[1])

    return False

def main():
    import sys
    grids = [[], [], []]
    for i, line in enumerate(sys.stdin.readlines()):
        lst = []
        for s in line.strip():
            lst.append(1 if s == '#' else 0)
        grids[i // 4].append(lst)
    # print(grids)
    print(YES if solve(grids) else NO)


if __name__ == "__main__":
    main()
