#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, A)


def solve(N: int, A: "List[int]"):
    return


if __name__ == "__main__":
    main()
