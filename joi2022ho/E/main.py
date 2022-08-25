#!/usr/bin/env python3



def solve(H: int, W: int, A: "List[List[int]]"):
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
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A)


if __name__ == "__main__":
    main()
