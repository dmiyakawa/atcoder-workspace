#!/usr/bin/env python3

import sys

def floor_sum(n: int, m: int, a: int, b: int) -> int:
    assert 1 <= n
    assert 1 <= m

    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    return ans


def solve(T: int, N: "List[int]", M: "List[int]", A: "List[int]", B: "List[int]"):
    for n, m, a, b in zip(N, M, A, B):
        print(floor_sum(n, m, a, b))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    N = [int()] * (T)  # type: "List[int]"
    M = [int()] * (T)  # type: "List[int]"
    A = [int()] * (T)  # type: "List[int]"
    B = [int()] * (T)  # type: "List[int]"
    for i in range(T):
        N[i] = int(next(tokens))
        M[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(T, N, M, A, B)


if __name__ == "__main__":
    main()
