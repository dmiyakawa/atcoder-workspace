#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(N: int, S: str, W: "List[int]"):
    from bisect import bisect
    c_lst = []
    a_lst = []
    for s, w in zip(S, W):
        if s == "1":
            a_lst.append(w)
        else:
            c_lst.append(w)
    if not c_lst or not a_lst:
        return N
    a_min, a_max = min(a_lst), max(a_lst)
    c_min, c_max = min(c_lst), max(c_lst)
    if c_max < a_min:
        return N

    a_lst.sort()
    c_lst.sort()
    max_count = 0
    for ai, val in enumerate(W):
        a = len(a_lst) - bisect(a_lst, val) + bisect(c_lst, val)
        b = len(a_lst) - bisect(a_lst, val - 0.1) + bisect(c_lst, val - 0.1)
        c = len(a_lst) - bisect(a_lst, val + 0.1) + bisect(c_lst, val + 0.1)
        max_count = max(max_count, a, b, c)
    return max_count


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, S, W))


if __name__ == "__main__":
    main()
