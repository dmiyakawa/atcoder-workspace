#!/usr/bin/env python3

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, p1: Point2D, p2: Point2D):
        self.p1 = p1
        self.p2 = p2

    @staticmethod
    def cross(x0, y0, x1, y1):
        """外積 outer product"""
        return x0 * y1 - y0 * x1

    def intersect(self, s: "LineSegment"):
        a, b = self.p1, self.p2
        c, d = s.p1, s.p2

        s = (a.x - b.x) * (c.y - a.y) - (a.y - b.y) * (c.x - a.x)
        t = (a.x - b.x) * (d.y - a.y) - (a.y - b.y) * (d.x - a.x)
        if s * t > 0:
            return False

        s = (c.x - d.x) * (a.y - c.y) - (c.y - d.y) * (a.x - c.x)
        t = (c.x - d.x) * (b.y - c.y) - (c.y - d.y) * (b.x - c.x)
        if s * t > 0:
            return False
        return True

    def get_cross_point(self, s: "LineSegment") -> "Tuple[float, float]":
        bx = s.p2.x - s.p1.x
        by = s.p2.y - s.p1.y

        d1 = abs(self.cross(bx, by, self.p1.x - s.p1.x, self.p1.y - s.p1.y))
        d2 = abs(self.cross(bx, by, self.p2.x - s.p1.x, self.p2.y - s.p1.y))
        t = d1 / (d1 + d2)
        return self.p1.x + (self.p2.x - self.p1.x) * t, self.p1.y + (self.p2.y - self.p1.y) * t


def detect_intersection(a, b, c, d):
    """線分abと線分cdが交差する場合True"""
    s = (a.x - b.x) * (c.y - a.y) - (a.y - b.y) * (c.x - a.x)
    t = (a.x - b.x) * (d.y - a.y) - (a.y - b.y) * (d.x - a.x)
    if s * t > 0:
        return False

    s = (c.x - d.x) * (a.y - c.y) - (c.y - d.y) * (a.x - c.x)
    t = (c.x - d.x) * (b.y - c.y) - (c.y - d.y) * (b.x - c.x)
    if s * t > 0:
        return False
    return True





def cgl_2_c():
    """https://onlinejudge.u-aizu.ac.jp/problems/CGL_2_C"""
    Q = int(input())
    for _ in range(Q):
        x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
        s1 = LineSegment(Point2D(x0, y0), Point2D(x1, y1))
        s2 = LineSegment(Point2D(x2, y2), Point2D(x3, y3))
        x, y = s1.get_cross_point(s2)
        print(x, y)


if __name__ == "__main__":
    cgl_2_c()

