#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = next(tokens)  # type: str
    solve(T)


def solve(T: str):
    return


if __name__ == "__main__":
    main()
