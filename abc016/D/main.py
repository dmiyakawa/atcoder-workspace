#!/usr/bin/env python3


def solve(A_x: int, A_y: int, B_x: int, B_y: int, N: int, X: "List[int]", Y: "List[int]"):
    points = [Point2D(x, y) for x, y in zip(X, Y)]
    segments = []
    for i, p in enumerate(points):
        if i == N - 1:
            segments.append(LineSegment(p, points[0]))
        else:
            segments.append(LineSegment(p, points[i + 1]))
    s1 = LineSegment(Point2D(A_x, A_y), Point2D(B_x, B_y))
    count = 0
    for s in segments:
        if s1.intersect(s):
            count += 1
    assert count % 2 == 0
    print(count // 2 + 1)


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)


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

    def __str__(self):
        return "{}-{}".format(self.p1, self.p2)

    __repr__ = __str__


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A_x = int(next(tokens))  # type: int
    A_y = int(next(tokens))  # type: int
    B_x = int(next(tokens))  # type: int
    B_y = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(A_x, A_y, B_x, B_y, N, X, Y)


if __name__ == "__main__":
    main()
