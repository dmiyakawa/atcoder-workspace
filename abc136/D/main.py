#!/usr/bin/env python3


def solve(S: str):
    N = len(S)
    l = 0
    A = [0] * N
    while l < N - 1:
        assert S[l] == "R"
        r = S.index("L", l)
        for i in range(l, r):
            A[i] = r - i
        c = -1
        while r < N and S[r] == "L":
            A[r] = c
            c -= 1
            r += 1
        l = r
    B = [0] * N
    for i, a in enumerate(A):
        if a > 0:
            index = i + a - (1 if abs(a) % 2 == 1 else 0)
        else:
            assert a < 0
            index = i + a + (1 if abs(a) % 2 == 1 else 0)
        B[index] += 1
    print(*B)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
