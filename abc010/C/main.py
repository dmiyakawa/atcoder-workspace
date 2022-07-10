#!/usr/bin/env python3
import math
import sys


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    tx_a = int(next(tokens))  # type: int
    ty_a = int(next(tokens))  # type: int
    tx_b = int(next(tokens))  # type: int
    ty_b = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    n = int(next(tokens))  # type: int
    x = [int()] * (n)  # type: "List[int]"
    y = [int()] * (n)  # type: "List[int]"
    for i in range(n):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    print("YES" if solve(tx_a, ty_a, tx_b, ty_b, T, V, n, x, y) else "NO")


def solve(tx_a: int, ty_a: int, tx_b: int, ty_b: int, T: int, V: int, n: int, X: "List[int]", Y: "List[int]"):
    for x, y in zip(X, Y):
        l = math.sqrt((x - tx_a) ** 2 + (y - ty_a) ** 2) + math.sqrt((x - tx_b)**2 + (y - ty_b)**2)
        if l <= V*T:
            return True
    return False


if __name__ == "__main__":
    main()
