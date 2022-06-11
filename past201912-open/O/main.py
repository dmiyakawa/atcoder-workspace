#!/usr/bin/env python3
#
# 解法ノート
# 「前回の操作で出た目」が所与のとき、それ以降の操作の期待値を考える
# サイコロの中の最大値をまず考えると、その試行で絶対に止まるので期待値は1.0
# 最大値の次に大きい数値を考えると、1.0 + 上の最大値のサイコロを振ったときの期待値(1/6)
# 一般には、「前回の操作で出た目X」を考えた際のそれ以降の期待値は 1.0 + それ以降（Xより大きい数字を全て処理したときの）の期待値となる。
# 「それ以降の期待値」は、それまでの期待値と、Xを含むサイコロの新たな期待値の大きい方を取る。
# Xより小さい数値はXを考えた際の期待値には影響しないので、「大きい順」に処理するのが重要
#
# 以上の操作をサイコロに登場する数 6 * N 個で大きい数字から順番に処理したあと「前回の操作で出た目」が 0 のときの結果を求めれば良い
#
# 座標圧縮からの期待値DP
# https://blog.hamayanhamayan.com/entry/2020/01/01/000510
#

from typing import Dict


def main():
    N = int(input())
    A = []
    values = []
    dice_map: Dict[int, int] = {}
    for i in range(N):
        lst = []
        A.append(lst)
        for e in input().split():
            v = int(e)
            lst.append(v)
            values.append(v)
            dice_map[v] = i
    values.sort(reverse=True)

    expectations: Dict[int, float] = {}
    current_max_expectation = 0
    for value in values:
        expectations[value] = 1.0 + current_max_expectation
        dice_id = dice_map[value]
        next_expectation = sum(expectations.get(value_2, 0) for value_2 in A[dice_id]) / 6
        current_max_expectation = max(current_max_expectation, next_expectation)

    # 最初の1回目に対応する 1 を足す
    print(1 + current_max_expectation)


if __name__ == "__main__":
    main()
