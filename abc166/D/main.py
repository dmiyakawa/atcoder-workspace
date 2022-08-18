#!/usr/bin/env python3



def solve(X: int):
    for a in range(-200, 201):
        for b in range(-200, 201):
            if X == a**5 - b**5:
                return a, b


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    print(*solve(X))


if __name__ == "__main__":
    main()
