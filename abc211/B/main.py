#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: "List[str]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(4)]  # type: "List[str]"
    solve(S)


if __name__ == "__main__":
    main()
