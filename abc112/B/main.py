#!/usr/bin/env python3



def solve(N: int, T: int, c: "List[int]", t: "List[int]"):
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
    T = int(next(tokens))  # type: int
    c = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        c[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, T, c, t)


if __name__ == "__main__":
    main()
