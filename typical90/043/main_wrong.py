#!/usr/bin/env python3

import heapq
from typing import Dict, Tuple

LEFT = "L"
RIGHT = "R"
UP = "U"
DOWN = "D"


def main():
    H, W = [int(e) for e in input().split()]
    sr, sc = [int(e) - 1 for e in input().split()]
    tr, tc = [int(e) - 1 for e in input().split()]
    MAX_VALUE: int = H * W
    maze = []
    for _ in range(H):
        maze.append(input())

    def _debug(pr, pc, direction):
        for r, row in enumerate(maze):
            lst = []
            for c, s in enumerate(row):
                if (pr, pc) == (r, c):
                    if direction == LEFT:
                        s = "<"
                    elif direction == RIGHT:
                        s = ">"
                    elif direction == UP:
                        s = "^"
                    else:
                        s = "v"
                elif (sr, sc) == (r, c):
                    s = "s"
                elif (tr, tc) == (r, c):
                    s = "t"
                lst.append(s)
            print("".join(lst))
        print()

    distance = abs(sr - tr) + abs(sc - tc)
    not_tried = [(0, distance, 0, sr, sc, LEFT),
                 (0, distance, 0, sr, sc, RIGHT),
                 (0, distance, 0, sr, sc, UP),
                 (0, distance, 0, sr, sc, DOWN)]
    heapq.heapify(not_tried)

    dp: Dict[Tuple[int, int, str], int] = {(sr, sc): 0}
    ended = False
    while not_tried:
        if ended:
            break
        t, distance, same_direction, r, c, d = heapq.heappop(not_tried)
        # _debug(r, c, d)
        if d == LEFT:
            next_moves = [(r, c - 1, LEFT, t), (r - 1, c, UP, t + 1), (r + 1, c, DOWN, t + 1)]
        elif d == RIGHT:
            next_moves = [(r, c + 1, RIGHT, t), (r - 1, c, UP, t + 1), (r + 1, c, DOWN, t + 1)]
        elif d == UP:
            next_moves = [(r - 1, c, UP, t), (r, c - 1, LEFT, t + 1), (r, c + 1, RIGHT, t + 1)]
        else:
            next_moves = [(r + 1, c, DOWN, t), (r, c - 1, LEFT, t + 1), (r, c + 1, RIGHT, t + 1)]

        for (next_r, next_c, next_d, next_t) in next_moves:
            if next_r < 0 or H <= next_r or next_c < 0 or W <= next_c or maze[next_r][next_c] == "#":
                continue
            if dp.get((next_r, next_c, next_d), MAX_VALUE) > next_t:
                dp[(next_r, next_c, next_d)] = next_t
                if (next_r, next_c) == (tr, tc):
                    ended = True
                    break
                next_distance = abs(next_r - tr) + abs(next_c - tc)
                same_direction = 0 if next_d == d else 1
                heapq.heappush(not_tried, (next_t, next_distance, same_direction, next_r, next_c, next_d))
    print(min(dp.get((tr, tc, LEFT), MAX_VALUE),
              dp.get((tr, tc, UP), MAX_VALUE),
              dp.get((tr, tc, RIGHT), MAX_VALUE),
              dp.get((tr, tc, DOWN), MAX_VALUE)),
          end="")


if __name__ == "__main__":
    main()
