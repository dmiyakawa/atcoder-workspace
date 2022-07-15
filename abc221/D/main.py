#!/usr/bin/env python3

import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    lst = [(a, 1) for a in A] + [(a + b, -1) for a, b in zip(A, B)]
    lst.sort()
    lst2 = []
    cur_day = 0
    cur_count = 0
    for a, c in lst:
        if cur_day == a:
            cur_count += c
        else:
            if cur_day > 0 and cur_count != 0:
                lst2.append((cur_day, cur_count))
            cur_day = a
            cur_count = c
    if cur_day > 0:
        lst2.append((cur_day, cur_count))

    cur_day = 0
    cur_count = 0
    d = {}
    for a, c in lst2:
        if cur_day > 0:
            d[cur_count] = d.get(cur_count, 0) + (a - cur_day)
        cur_day = a
        cur_count += c

    if cur_day > 0:
        d[cur_count] = d.get(cur_count, 0) + (10**100 - cur_day)
    print(*[d.get(k, 0) for k in range(1, N + 1)])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == "__main__":
    main()
