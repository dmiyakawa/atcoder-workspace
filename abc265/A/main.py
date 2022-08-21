#!/usr/bin/env python3



def solve(X: int, Y: int, N: int):
    min_val = 10**9
    for a in range(100):
        for b in range(100):
            if a + b * 3 == N:
                min_val = min(min_val, a * X + b * Y)
    print(min_val)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(X, Y, N)


if __name__ == "__main__":
    main()
