#!/usr/bin/env python3



def solve(M: int, D: int):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(M, D)


if __name__ == "__main__":
    main()
