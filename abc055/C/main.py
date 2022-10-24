#!/usr/bin/env python3


def solve(N: int, M: int):
    if M - N * 2 <= 0:
        ans = M // 2
    else:
        ans = (M - N * 2) // 4 + N
    print(ans)


def solve_1(N: int, M: int):
    l, r = 0, N + M
    while l + 1 < r:
        m = (l + r) // 2
        if N >= m:
            if M >= m * 2:
                l = m
            else:
                r = m
        else:
            if M >= m * 2 and N + (M - m * 2) // 2 >= m:
                l = m
            else:
                r = m
    print(l)



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
