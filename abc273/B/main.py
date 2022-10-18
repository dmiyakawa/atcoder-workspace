#!/usr/bin/env python3



def solve(X: int, K: int):
    x = X
    for i in range(K):
        l = x // 10**i % 10
        if l >= 5:
            x = x - l * 10**i + 10**(i + 1)
        else:
            x = x - l * 10**i
    print(x)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(X, K)


if __name__ == "__main__":
    main()
