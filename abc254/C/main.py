#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, K: int, a_lst: "List[int]"):
    from itertools import zip_longest
    k_lst = [[] for _ in range(K)]
    for i, a in enumerate(a_lst):
        k_lst[i % K].append(a)

    for lst in k_lst:
        lst.sort()

    cur = 0
    for values in zip_longest(*k_lst):
        for value in values:
            if value is None:
                continue
            if cur > value:
                return False
            cur = value
    return True


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(YES if solve(N, K, a) else NO)


if __name__ == "__main__":
    main()
