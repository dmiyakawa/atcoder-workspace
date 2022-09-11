#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    print(YES if T.startswith(S) else NO)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == "__main__":
    main()
