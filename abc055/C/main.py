#!/usr/bin/env python3



def solve(N: int, M: int):
    x = 2 * (M - N) // 5
    print(N + x)



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


if __name__ == "__main__":
    main()