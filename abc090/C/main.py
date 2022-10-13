#!/usr/bin/env python3



def solve(N: int, M: int):
    if N == 1:
        if M == 1:
            return 1
        elif M == 2:
            return 0
        else:
            return M - 2
    elif N == 2:
        return 0
    else:
        if M == 1:
            return N - 2
        elif M == 2:
            return 0
        else:
            return (N - 2) * (M - 2)


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
    print(solve(N, M))


if __name__ == "__main__":
    main()
