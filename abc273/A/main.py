#!/usr/bin/env python3



def solve(N: int):
    if N == 0:
        return 1
    else:
        return N * solve(N - 1)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    print(solve(N))


if __name__ == "__main__":
    main()
