#!/usr/bin/env python3



def solve(N: int, d: "List[int]", x: int):
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
    d = [int(next(tokens)) for _ in range(1)]  # type: "List[int]"
    x = int(next(tokens))  # type: int
    solve(N, d, x)


if __name__ == "__main__":
    main()
