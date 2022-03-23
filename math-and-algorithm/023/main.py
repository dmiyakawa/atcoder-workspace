#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    R = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, B, R)


def solve(N: int, B: "List[int]", R: "List[int]"):
    return


if __name__ == "__main__":
    main()
