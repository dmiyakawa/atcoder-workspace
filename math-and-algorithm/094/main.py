#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, B)


def solve(N: int, B: "List[int]"):
    return


if __name__ == "__main__":
    main()
