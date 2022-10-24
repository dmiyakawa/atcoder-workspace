#!/usr/bin/env python3



def solve(N: int, Q: int, q: "List[int]"):
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
    Q = int(next(tokens))  # type: int
    q = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, q)


if __name__ == "__main__":
    main()
