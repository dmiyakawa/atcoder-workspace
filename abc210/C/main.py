#!/usr/bin/env python3



def solve(N: int, K: int, c: "List[int]"):
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
    K = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, c)


if __name__ == "__main__":
    main()
