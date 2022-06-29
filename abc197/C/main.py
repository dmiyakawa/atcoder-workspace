#!/usr/bin/env python3


def main_ans():
    # bit全探索
    # https://atcoder.jp/contests/abc197/editorial/997
    N = int(input())
    A = [int(e) for e in input().split()]
    min_n = 10**31
    for n in range(2**(N-1)):
        xor_ed = 0
        or_ed = 0
        for j in range(N):
            or_ed |= A[j]
            if n >> j & 1 or j == N - 1:
                xor_ed ^= or_ed
                or_ed = 0
        min_n = min(min_n, xor_ed)
    print(min_n)


def gen_combs(comb, rest):
    for i in range(1, len(rest)):
        yield from gen_combs(comb + [rest[:i]], rest[i:])
    yield comb + [rest]


def main():
    from functools import reduce
    # AC版
    N = int(input())
    A = [int(e) for e in input().split()]
    min_n = 10**31
    g = gen_combs([], A)
    for lst in g:
        n = reduce(lambda x, y: x ^ y, [reduce(lambda x, y: x | y, sub) for sub in lst])
        # print(lst, n)
        min_n = min(min_n, n)
    print(min_n)


if __name__ == "__main__":
    main_ans()
