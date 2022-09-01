#!/usr/bin/env python3

def solve_ref(N: int, M: int, A: "List[int]"):
    import math
    ks = {v for v in range(1, M + 1)}
    for a in sorted(set(A)):
        to_remove = set()
        for k in ks:
            if math.gcd(k, a) != 1:
                to_remove.add(k)
        ks -= to_remove

    print(len(ks))
    for k in sorted(ks):
        print(k)


def solve(N: int, M: int, A: "List[int]"):
    s = set()
    for a in A:
        if a == 1:
            continue
        d = factorize_in_prime(a)
        s |= set(d.keys())

    ans = []
    for k in range(1, M + 1):
        if k == 1:
            ans.append(k)
            continue
        d = factorize_in_prime(k)
        if not (set(d.keys()) & s):
            ans.append(k)

    print(len(ans))
    for v in ans:
        print(v)


def factorize_in_prime(n) -> "Dict[int, int]":
    """2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す"""
    # https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
    assert n >= 2
    d = {}
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                count += 1
                temp //= i
            d[i] = count

    if temp != 1:
        d[temp] = 1

    if not d:
        d[n] = 1

    return d

def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
