#!/usr/bin/env python3

from typing import Dict

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    S = next(tokens)  # type: str
    solve(N, X, Y, S)


def solve(N: int, X: "List[int]", Y: "List[int]", S: str):
    # 右を向いていて一番座標の小さい人
    # key: Y座標, value: X座標
    y_to_right: Dict[int, int] = {}
    # 左を向いていて一番座標の大きい人
    # key: Y座標, value: X座標
    y_to_left: Dict[int, int] = {}
    for (x, y, s) in zip(X, Y, S):
        if s == "L" and (y not in y_to_left or y_to_left[y] < x):
            y_to_left[y] = x
        elif s == "R" and (y not in y_to_right or x < y_to_right[y]):
            y_to_right[y] = x

    collision_happens = False
    for y in y_to_right:
        if y in y_to_left and y_to_right[y] < y_to_left[y]:
            collision_happens = True
            break
    print(YES if collision_happens else NO, end="")


if __name__ == "__main__":
    main()
