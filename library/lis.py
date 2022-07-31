#!/usr/bin/env python3
#
# 最長増加部分列 (LIS: Longest Increasing Subsequence) を求める例
# lis = [-Inf, Inf, ...] で初期化し
#

from bisect import bisect_left
from typing import List

Inf = float("Inf")


class LIS:
    def __init__(self, n):
        self._n = n
        self._seq = [Inf] * (n + 1)
        self._seq[0] = -Inf
        self._max_index = 0

    def insert(self, value):
        index = bisect_left(self._seq, value)
        self._seq[index] = value
        self._max_index = max(index, self._max_index)

    def get_raw_sequence(self) -> List[float]:
        return self._seq

    def get_lis(self):
        return self._seq[1:self._max_index + 1]


def _main():
    """\
    https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_D
    """
    N = int(input())
    lis = LIS(N)
    for _ in range(N):
        lis.insert(int(input()))
    print(len(lis.get_lis()))


if __name__ == "__main__":
    _main()
