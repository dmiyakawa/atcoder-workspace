#!/usr/bin/env python3

import itertools
import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, K, S)


def solve(N: int, K: int, S: "List[str]"):
    max_num_ks = 0
    # 32767 * 15 * 26
    for r in range(K, N + 1):
        for comb in itertools.combinations(S, r):
            nums = {}
            for s in comb:
                for ch in s:
                    nums[ch] = nums.get(ch, 0) + 1
            num_ks = 0
            for key, value in nums.items():
                if value == K:
                    num_ks += 1
            max_num_ks = max(num_ks, max_num_ks)
    print(max_num_ks)


if __name__ == "__main__":
    main()
