#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: int, B: int, C: int, s: "List[str]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, A, B, C, s)


if __name__ == "__main__":
    main()
