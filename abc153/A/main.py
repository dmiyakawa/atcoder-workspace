#!/usr/bin/env python3



def solve(H: int, A: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    solve(H, A)


if __name__ == "__main__":
    main()
