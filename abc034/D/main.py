#!/usr/bin/env python3



def solve(N: int, K: int, w: "List[int]", p: "List[int]"):
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
    w = [int()] * (N)  # type: "List[int]"
    p = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        p[i] = int(next(tokens))
    solve(N, K, w, p)


if __name__ == "__main__":
    main()
