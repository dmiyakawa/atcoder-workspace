#!/usr/bin/env python3

import math


# TODO: 後で整形する
class Vector:
    """c.f https://atcoder.jp/contests/abc139/submissions/34704456"""

    def __init__(self, x, y, init_x=1, init_y=0):
        self.x = x
        self.y = y
        self.norm2 = x * x + y * y
        self.norm = self.norm2 ** 0.5
        self.zone = 2
        if x == y == 0:
            self.zone = -1
        elif init_x * y - init_y * x > 0:
            self.zone = 1
        elif init_x * y - init_y * x < 0:
            self.zone = 3
        elif init_x * x + init_y * y > 0:
            self.zone = 0

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if self.zone != other.zone: return False
        return self.outer(other) == 0

    def __lt__(self, other):
        """偏角に基づく比較。例外的に (0, 0) が最小"""
        if self.zone == other.zone:
            return self.outer(other) > 0
        return self.zone < other.zone

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    #
    # def __iadd__(self, other):
    #     self.x += other.x
    #     self.y += other.y
    #     return self
    #
    # def __isub__(self, other):
    #     self.x -= other.x
    #     self.y -= other.y
    #     return self

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, val):
        return Vector(val * self.x, val * self.y)

    __rmul__ = __mul__

    def __truediv__(self, val):
        assert val != 0
        return Vector(self.x / val, self.y / val)

    def dot(self, v):
        return self.x * v.x + self.y * v.y

    def outer(self, v):
        return self.x * v.y - self.y * v.x

    def rot90(self):
        return Vector(-self.y, self.x)


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, v: "Vector2D"):
        """内積 inner product"""
        return self.x * v.x + self.y * v.y

    def cross(self, v: "Vector2D"):
        """外積 outer product"""
        return self.x * v.y - self.y * v.x

    def hypot(self):
        """原点からの距離（ユークリッドノルム）を返す。
        hypotenuseは直角三角形の斜辺のこと"""
        return math.hypot(self.x, self.y)

    def rotate(self, rad: float) -> "Vector":
        """原点を中心にr rad回転させたベクトルを返す"""
        if (self.x, self.y) == (0, 0):
            return Vector2D(0, 0)
        hypot = self.hypot()
        theta = math.atan2(self.y, self.x)
        return Vector2D(hypot * math.cos(theta + rad), hypot * math.sin(theta + rad))

    def is_orthogonal(self, v: "Vector2D"):
        """与えられたベクトルが直交しているときにTrue"""
        return self.dot(v) == 0

    def is_parallel(self, v: "Vector2D"):
        """このベクトルが乗る直線と与えられたベクトルが乗る直線が平行なときにTrue"""
        return self.cross(v) == 0

    def __repr__(self):
        return "Vector2D(x={}, y={})".format(self.x, self.y)


def abc259_b():
    """https://atcoder.jp/contests/abc259/tasks/abc259_b"""
    a, b, d = map(int, input().split())
    v = Vector2D(a, b).rotate(d * math.pi / 180)
    print("{:.10f}".format(v.x), "{:.10f}".format(v.y))


def cgl_2_a():
    """https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_A"""
    n = int(input())
    for _ in range(n):
        x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
        v1 = Vector2D(x1 - x0, y1 - y0)
        v2 = Vector2D(x3 - x2, y3 - y2)
        if v1.is_orthogonal(v2):
            print(1)
        elif v1.is_parallel(v2):
            print(2)
        else:
            print(0)


if __name__ == "__main__":
    cgl_2_a()
    # abc259_b()
    pass


