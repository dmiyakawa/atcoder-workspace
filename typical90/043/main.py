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

    not_tried = [(0, sr, sc, LEFT), (0, sr, sc, RIGHT), (0, sr, sc, UP), (0, sr, sc, DOWN)]
    heapq.heapify(not_tried)

    dp: Dict[Tuple[int, int, str], int] = {(sr, sc, LEFT): 0, (sr, sc, RIGHT): 0,
                                           (sr, sc, UP): 0, (sr, sc, DOWN): 0}
    current_minimum_t = MAX_VALUE
    ended = False
    while not_tried:
        if ended:
            break
        t, r, c, d = heapq.heappop(not_tried)
        if current_minimum_t < t:
            break
        # _debug(r, c, d)

        def check(tup):
            r2, c2, d2, t2 = tup
            return 0 <= r2 < H and 0 <= c2 < W and dp.get((r2, c2, d2), MAX_VALUE) > t2 and maze[r2][c2] == "."

        if d == LEFT:
            next_moves = filter(check, [(r, c - 1, LEFT, t), (r - 1, c, UP, t + 1), (r + 1, c, DOWN, t + 1)])
        elif d == RIGHT:
            next_moves = filter(check, [(r, c + 1, RIGHT, t), (r - 1, c, UP, t + 1), (r + 1, c, DOWN, t + 1)])
        elif d == UP:
            next_moves = filter(check, [(r - 1, c, UP, t), (r, c - 1, LEFT, t + 1), (r, c + 1, RIGHT, t + 1)])
        else:
            next_moves = filter(check, [(r + 1, c, DOWN, t), (r, c - 1, LEFT, t + 1), (r, c + 1, RIGHT, t + 1)])

        for (next_r, next_c, next_d, next_t) in next_moves:
            if dp.get((next_r, next_c, next_d), MAX_VALUE) > next_t and current_minimum_t > next_t:
                dp[(next_r, next_c, next_d)] = next_t
                if (next_r, next_c) == (tr, tc):
                    current_minimum_t = next_t
                # _debug(next_r, next_c, next_t)
                heapq.heappush(not_tried, (next_t, next_r, next_c, next_d))
    print(min(dp.get((tr, tc, LEFT), MAX_VALUE),
              dp.get((tr, tc, UP), MAX_VALUE),
              dp.get((tr, tc, RIGHT), MAX_VALUE),
              dp.get((tr, tc, DOWN), MAX_VALUE)),
          end="")


if __name__ == "__main__":
    main()
