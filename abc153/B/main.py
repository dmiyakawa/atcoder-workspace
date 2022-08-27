#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, N: int, A: "List[int]"):
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
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(H, N, A)


if __name__ == "__main__":
    main()
