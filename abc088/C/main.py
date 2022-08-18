#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(c: "List[List[int]]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    c = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    solve(c)


if __name__ == "__main__":
    main()
