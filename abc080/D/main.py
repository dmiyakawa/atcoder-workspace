#!/usr/bin/env python3



def solve(N: int, C: int, s: "List[int]", t: "List[int]", c: "List[int]"):
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
    C = int(next(tokens))  # type: int
    s = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, s, t, c)


if __name__ == "__main__":
    main()
