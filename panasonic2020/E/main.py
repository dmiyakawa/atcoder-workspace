#!/usr/bin/env python3



def solve(a: str, b: str, c: str):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = next(tokens)  # type: str
    b = next(tokens)  # type: str
    c = next(tokens)  # type: str
    solve(a, b, c)


if __name__ == "__main__":
    main()
