#!/usr/bin/env python3
#
# RMQ (Range Minimum Query) を実現するセグメント木
#
#
# See also
# https://www.slideshare.net/iwiwi/ss-3578491
#
# ref.
# http://poj.org/problem?id=2991a
#


class SegmentTreeForRMQ:
    def __init__(self, n, *, max_value=2 ** 63):
        """要素数nのセグメント木を作る"""
        self.n = n
        self.max_value = max_value
        m = 1
        while m < n:
            m *= 2
        self.dat = [max_value] * (2 * m)

    @classmethod
    def init_with_values(cls, values) -> "SegmentTreeForRMQ":
        tree = cls(len(values))
        for i, value in enumerate(values):
            tree.update(i, value)
        return tree

    def update(self, k, a):
        """index kの要素をaに変更する"""
        k += self.n - 1
        self.dat[k] = a
        # 木を親方向にたどりながら経路にあるノード更新する
        while k > 0:
            k = (k - 1) // 2
            self.dat[k] = min(self.dat[k * 2 + 1], self.dat[k * 2 + 2])

    def query_rmq(self, a, b, k=0, left=0, right=None):
        """\
        [a, b)の最小値を求める
        """
        right = right or self.n
        if right <= a or b <= left:
            return self.max_value
        elif a <= left and right <= b:
            return self.dat[k]
        else:
            left_value = self.query_rmq(a, b, k * 2 + 1, left, (left + right) // 2)
            right_value = self.query_rmq(a, b, k * 2 + 2, (left + right) // 2, right)
            return min(left_value, right_value)


def main():
    tree = SegmentTreeForRMQ.init_with_values([5, 3, 7, 9, 6, 4, 1, 2])
    print(tree.dat)
    print(tree.query_rmq(1, 8))


if __name__ == "__main__":
    main()

