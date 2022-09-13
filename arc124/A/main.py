#!/usr/bin/env python3

MOD = 998244353  # type: int


def solve(N: int, K: int, c: "List[str]", k: "List[int]"):
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
    c = [str()] * (K)  # type: "List[str]"
    k = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        c[i] = next(tokens)
        k[i] = int(next(tokens))
    solve(N, K, c, k)


if __name__ == "__main__":
    main()
