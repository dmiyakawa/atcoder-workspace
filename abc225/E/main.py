#!/usr/bin/env python3


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __lt__(self, o):
        return self.num * o.den < o.num * self.den

    def __le__(self, o):
        return self.num * o.den <= o.num * self.den


def main():
    # import math
    N = int(input())
    Fs = []

    for i in range(N):
        x, y = [int(e) for e in input().split()]
        # 偏角2つをもとにした区間スケジューリング問題ではあるが、
        # 偏角でソートするといっても、素直にatan2を使うと割り算で発生する誤差でWAが発生する (022.txt)
        # srad = math.atan2(y - 1, x)
        # erad = math.atan2(y, x - 1)
        # srad = (y - 1) * x
        # erad = y * (x - 1)
        # Fs.append((erad, srad))
        Fs.append((Fraction(y, x - 1), Fraction(y - 1, x)))
    Fs.sort()
    ans = 0
    last_i = None
    for i in range(N):
        if last_i is None or Fs[last_i][0] <= Fs[i][1]:
            ans += 1
            last_i = i
    print(ans)


def main_ref():
    # https://atcoder.jp/contests/abc225/submissions/33558104
    N = int(input())
    ps = []
    for _ in range(N):
        x, y = map(int, input().split())
        ps.append((Fraction(y, x - 1), Fraction(y - 1, x)))

    ps.sort()
    ans = 1
    now = ps[0][0]
    for a, b in ps[1:]:
        if now <= b:
            ans += 1
            now = a

    print(ans)


if __name__ == "__main__":
    main()
