#!/usr/bin/env python3


MOD = 100  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


def solve(N: int, a: "List[int]"):
    return


if __name__ == "__main__":
    main()