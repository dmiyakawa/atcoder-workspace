#!/usr/bin/env python3



def solve(R: int, C: int, A: "List[List[int]]", B: "List[List[int]]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(C - 1)] for _ in range(R)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(C)] for _ in range(R - 1)]  # type: "List[List[int]]"
    solve(R, C, A, B)


if __name__ == "__main__":
    main()
