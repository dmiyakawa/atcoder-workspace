#!/usr/bin/env python3



def solve(K: int, N: int, v: "List[int]", w: "List[str]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    v = [int()] * (N)  # type: "List[int]"
    w = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        v[i] = int(next(tokens))
        w[i] = next(tokens)
    solve(K, N, v, w)


if __name__ == "__main__":
    main()
