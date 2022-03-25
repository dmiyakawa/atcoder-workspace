#!/usr/bin/env python3


MOD = 1000000007  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


def pow_int_with_mod(x: int, y: int, m: int) -> int:
    """\
    x^y mod m を返す。x, y, mはすべて正の整数とする
    x, y は10^9など非常に大きい際にもmを用いてそこそこ高速に動作することを目標とする
    """
    assert x > 0 and isinstance(x, int)
    assert y > 0 and isinstance(y, int)
    assert m > 0 and isinstance(m, int)
    if x < 1000 or y < 1000:
        return int(x ** y % m)
    y_rem = y
    to_be_multiplied = x % MOD
    ans = 1
    while y_rem:
        to_multiply = to_be_multiplied ** (y_rem % 10) % m
        ans = (ans * to_multiply) % m
        to_be_multiplied = (to_be_multiplied ** 10) % m
        y_rem //= 10
    return ans


def solve(N: int, K: int):
    ans: int
    if N == 1:
        ans = K % MOD
    elif N == 2:
        ans = K * (K - 1) % MOD
    else:
        ans = K * (K - 1) % MOD
        to_be_multiplied = K - 2
        rem = N - 2
        while rem:
            mul = to_be_multiplied ** (rem % 10) % MOD
            ans = ans * mul % MOD
            to_be_multiplied = to_be_multiplied ** 10 % MOD
            rem = rem // 10
    print(ans, end="")


if __name__ == "__main__":
    main()
