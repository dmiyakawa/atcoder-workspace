#!/usr/bin/env python3

import sys
from collections import defaultdict, Counter
from typing import List

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


MOD = 10  # type: int


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    print(solve(N, S))


def solve(N: int, S: "List[str]"):
    nums: List[Counter[int]] = [Counter(int(s[i]) for s in S) for i in range(10)]
    # print(nums)
    d = {}
    for t in range(N * 10):
        counter = nums[t % 10]
        # print(t, counter)
        for key in counter.keys():
            if counter[key] == 0:
                continue
            counter[key] -= 1
            d[key] = d.get(key, 0) + 1
            # print(key, d)
            if d[key] == N:
                return t


if __name__ == "__main__":
    main()
