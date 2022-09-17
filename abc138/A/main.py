#!/usr/bin/env python3



def solve(a: int, s: str):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    s = next(tokens)  # type: str
    solve(a, s)


if __name__ == "__main__":
    main()
