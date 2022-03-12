#!/usr/bin/env python3


MOD = 1000000007  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, B, K, c)


def solve(N: int, B: int, K: int, c: "List[int]"):
    return


if __name__ == "__main__":
    main()
