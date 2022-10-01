#!/usr/bin/env python3

def main():
    """初AC 満点
    解説とロジックが違うので説明。

    単に (x, y) で昇順にソートして3つずつ選んだだけ。これで問題の条件を満たすことを証明できる

    - 同じx座標上で並ぶ点は2つまで
    - あるx座標で2点取ってそのx座標のすぐ右側の点を選んで三角形を作る（2点あるなら下を選ぶ）
      - すると、その三角形の中には明らかに他の点がない。あるなら、「すぐ右側の点」の条件を満たさない
    - あるx座標で1点（2点あるなら上を選ぶ）選び、すぐ右側の点を2点選ぶ（2点候補があるなら下を選ぶ）
      - この3つも同じ直線上にいないので三角形になる
      - そして、やはり、この三角形の中には他の点がない
    - 上記のようにして構築した三角形は交差しあわない交差するなら「すぐ右側の点」の条件を満たしていない
    - よって今回の条件を満たした。
    """
    import sys
    input = sys.stdin.readline
    N = 300
    points = []
    for i in range(1, N + 1):
        x, y = map(int, input().split())
        points.append((x, y, i))
    sp = sorted(points)
    ans = []
    for i in range(0, N, 3):
        ans.append((sp[i][2], sp[i + 1][2], sp[i + 2][2]))

    # _check(points, ans):
    print(len(ans))
    for a in ans:
        print(a[0], a[1], a[2])



def _check(points, ans):
    v = [Vector2D(p[0], p[1]) for p in points]
    for i, tup in enumerate(ans):
        a, b, c = v[tup[0]], v[tup[1]], v[tup[2]]
        for o in v:
            if (o.x, o.y) in [(a.x, a.y), (b.x, b.y), (c.x, c.y)]:
                continue
            av, bv, cv = a - o, b - o, c - o
            s1 = av.cross(bv) > 0
            s2 = bv.cross(cv) > 0
            s3 = cv.cross(av) > 0
            if s1 == s2 == s3:
                print("{}'s answer is wrong ({}, {}, {}), ({}, {}, {}, {})".format(i, s1, s2, s3, o, a, b, c))
                return False
    return True


class Vector2D:
    """2次元座標上のベクトル。同時に単なる点としても使うことがある"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, v: "Vector2D"):
        """内積 inner product"""
        return self.x * v.x + self.y * v.y

    def cross(self, v: "Vector2D"):
        """外積 outer product"""
        return self.x * v.y - self.y * v.x

    def __add__(self, other) -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)


if __name__ == "__main__":
    main()
