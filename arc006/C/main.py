#!/usr/bin/env python3



def solve(N: int, w: "List[int]"):
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
    w = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, w)


if __name__ == "__main__":
    main()
