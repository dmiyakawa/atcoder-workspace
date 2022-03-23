#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, V)


def solve(N: int, K: int, V: "List[int]"):
    return


if __name__ == "__main__":
    main()
