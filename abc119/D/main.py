#!/usr/bin/env python3



def solve(A: int, B: int, Q: int, s: "List[int]", t: "List[int]", x: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    t = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(A, B, Q, s, t, x)


if __name__ == "__main__":
    main()
