#!/usr/bin/env python3
from functools import lru_cache


def solve(B: "List[List[int]]", C: "List[List[int]]"):

    def _debug(state):
        lst = [["?"] * 3 for _ in range(3)]
        for i in range(9):
            h, w = divmod(i, 3)
            v = (state // 3**i) % 3
            if v == 1:
                lst[h][w] = "o"
            elif v == 2:
                lst[h][w] = "x"
        print("\n".join(["".join(l) for l in lst]))
        print()


    @lru_cache(10**8)
    def handle_turn(state) -> "Tuple[int, int]":
        _debug(state)
        a_set = set()
        b_set = set()
        for i in range(9):
            v = (state // (3**i)) % 3
            if v == 1:
                a_set.add(i)
            elif v == 2:
                b_set.add(i)
        t = len(a_set) + len(b_set)
        if t == 9:
            a_score = 0
            b_score = 0
            for i in range(3):
                for j in range(3):
                    v = 3 ** i - 1 + j
                    if i < 3 and v in a_set and v + 9 in a_set:
                        a_score += B[i][j]
                    else:
                        b_score += B[i][j]
                    if j < 3 and v in a_set and v + 1 in a_set:
                        a_score += C[i][j]
                    else:
                        b_score += C[i][j]
            return a_score, b_score
        cur_turn = t % 2 + 1
        max_a = 0
        max_b = 0
        for i in range(9):
            v = (state // 3**i) % 3
            if v == 0:
                print(f"cur_turn: {cur_turn}, state: {state}, i: {i}, v: {v} next: {state | (cur_turn * 3**i)}")
                _a, _b = handle_turn(state | (cur_turn + 3**i))
                if cur_turn == 1:
                    if _a - _b > max_a - max_b:
                        max_a, max_b = _a, _b
                else:
                    if _b - _a > max_b - max_a:
                        max_a, max_b = _a, _b
        return max_a, max_b

    a, b = handle_turn(0)
    print(a)
    print(b)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    b = [[int(next(tokens)) for _ in range(3)] for _ in range(2)]  # type: "List[List[int]]"
    c = [[int(next(tokens)) for _ in range(2)] for _ in range(3)]  # type: "List[List[int]]"
    solve(b, c)


if __name__ == "__main__":
    main()
