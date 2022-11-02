#!/usr/bin/env python3
import bisect


def solve(N: int, M: int):
    divs = make_divisors(M)
    i = bisect.bisect_left(divs, N)
    # print(N, M, divs)
    if i < len(divs):
        ret = M // divs[i]
    else:
        ret = 1
    print(ret)


def make_divisors(n):
    """nの約数を列挙する"""
    # https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


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
