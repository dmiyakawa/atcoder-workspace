#!/usr/bin/env python3



def solve(ABCD: str):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    ABCD = next(tokens)  # type: str
    solve(ABCD)


if __name__ == "__main__":
    main()
