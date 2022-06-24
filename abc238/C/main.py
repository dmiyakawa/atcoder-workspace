#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 998244353  # type: int

def g(n):
    return 10**n - 10**(n - 1)


def main():
    N = int(input())
    ans = 0
    n = 1
    while True:
        last = n * 10 - 1 >= N
        v = min(n * 10 - 1, N)
        tmp = ["0"] * len(str(v))
        tmp[0] = "1"
        m = int("".join(tmp))
        l = v - m + 1
        # 等差数列の和の公式
        s = l*(1 + l) // 2
        ans += s
        ans %= MOD
        if last:
            break
        n *= 10
    print(ans)


if __name__ == "__main__":
    main()
