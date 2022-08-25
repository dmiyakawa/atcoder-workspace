#!/usr/bin/env python3

def main():
    """初AC"""
    from collections import Counter
    from functools import reduce
    from math import factorial
    S = input()
    c = Counter(S)
    ans = 0
    for ch in S:
        for key in sorted(c.keys()):
            if key == ch:
                break
            if c[key] == 0:
                continue
            num_rems = sum(c.values()) - 1
            rems = [factorial(nums - 1 if key0 == key else nums) for key0, nums in c.items()]
            ans += factorial(num_rems) // reduce(lambda x, y: x * y, rems)
        if c[ch] == 1:
            del c[ch]
        else:
            c[ch] -= 1
    print(ans + 1)


def main_2():
    """\
    https://atcoder.jp/contests/joisc2007/submissions/29358005 を参考にしたバージョン
    26 が若干マジカルワード気味でNと混同してバグることが多かった。慣れ
    """
    from math import factorial
    a = ord("A")
    S = [ord(ch) - a for ch in input()]
    N = len(S)
    counts = [0] * 26
    for ch in S:
        counts[ch] += 1
    fc = [factorial(n) for n in range(21)]

    ans = 0
    for i, v in enumerate(S):
        for j in range(26):
            if j == v:
                break
            if counts[j] == 0:
                continue
            cnt = fc[N - i - 1]
            for l in range(26):
                cnt //= fc[counts[l] - 1] if l == j else fc[counts[l]]
            ans += cnt
        counts[v] -= 1
    print(ans + 1)


if __name__ == "__main__":
    main_2()
