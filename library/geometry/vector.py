#!/usr/bin/env python3

import math


# TODO: 後で整形する
class Vector:
    """偏角ソートに対応した2次元ベクトル
    c.f https://atcoder.jp/contests/abc139/submissions/34704456
    """

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
        if self.zone != other.zone:
            return False
        return self.outer(other) == 0

    def __lt__(self, other):
        """偏角に基づく比較。(0, 0) は最小値と判定される"""
        if self.zone == other.zone:
            return self.outer(other) > 0
        return self.zone < other.zone

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

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

    def hypot(self):
        """原点からの距離（ユークリッドノルム）を返す。
        hypotenuseは直角三角形の斜辺のこと"""
        return math.hypot(self.x, self.y)

    def projection(self, v: "Vector2D") -> "Vector2D":
        """vが定める直線に正射影したベクトルを返す"""
        assert not (v.x, v.y) == (0, 0)
        den = v.x * v.x + v.y * v.y
        dot = self.dot(v)
        return Vector2D(dot * v.x / den, dot * v.y / den)

    def reflection(self, v: "Vector2D") -> "Vector2D":
        """vが定める直線に対する反射を返す"""
        assert not (v.x, v.y) == (0, 0)
        den = v.x * v.x + v.y * v.y
        dot = self.dot(v)
        return Vector2D(2 * dot * v.x / den - self.x, 2 * dot * v.y / den - self.y)

    def rotate(self, rad: float) -> "Vector2D":
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

    def __add__(self, other) -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self) -> "Vector2D":
        return Vector2D(-self.x, -self.y)

    def __mul__(self, val) -> "Vector2D":
        return Vector2D(val * self.x, val * self.y)

    def __repr__(self):
        return "Vector2D(x={}, y={})".format(self.x, self.y)

    @staticmethod
    def find_convex(lst: "List[Vector2D]", eps=1e-10, sort_first=True) -> "List[Vector2D]":
        """アンドリューのアルゴリズムを用いて凸包を時計回りで返す。引数で与えられたリストと同じリストを返すことがある"""
        if sort_first:
            lst.sort(key=lambda v: (v.x, v.y))
        N = len(lst)
        if N < 3:
            return lst
        u, l = [lst[0], lst[1]], [lst[-1], lst[-2]]

        # 凸包の上部
        for i in range(2, N):
            n = len(u)
            while n >= 2:
                v1 = u[n - 1] - u[n - 2]
                v2 = lst[i] - u[n - 2]
                if not (v1.cross(v2) > eps):
                    break
                u.pop()
                n -= 1
            u.append(lst[i])
        # 凸包の下部
        for i in range(N - 3, -1, -1):
            n = len(l)
            while n >= 2:
                v1 = l[n - 1] - l[n - 2]
                v2 = lst[i] - l[n - 2]
                if not (v1.cross(v2) > eps):
                    break
                l.pop()
                n -= 1
            l.append(lst[i])
        l.reverse()
        for i in range(len(u) - 2, 0, -1):
            l.append(u[i])
        return l


def abc259_b():
    """https://atcoder.jp/contests/abc259/tasks/abc259_b"""
    a, b, d = map(int, input().split())
    v = Vector2D(a, b).rotate(d * math.pi / 180)
    print("{:.10f}".format(v.x), "{:.10f}".format(v.y))


def cgl_1_a():
    """正射影を求める問題
    https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/all/CGL_1_A
    """
    x_p1, y_p1, x_p2, y_p2 = map(int, input().split())
    v1 = Vector2D(x_p2 - x_p1, y_p2 - y_p1)
    q = int(input())
    for _ in range(q):
        x_p, y_p = map(int, input().split())
        v2 = Vector2D(x_p - x_p1, y_p - y_p1)
        v = v2.projection(v1)
        print("{:.10f}".format(v.x + x_p1), "{:.10f}".format(v.y + y_p1))


def cgl_1_b():
    """反射を求める問題 https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/all/CGL_1_B"""
    x_p1, y_p1, x_p2, y_p2 = map(int, input().split())
    v1 = Vector2D(x_p2 - x_p1, y_p2 - y_p1)
    q = int(input())
    for _ in range(q):
        x_p, y_p = map(int, input().split())
        v2 = Vector2D(x_p - x_p1, y_p - y_p1)
        v = v2.reflection(v1)
        print("{:.10f}".format(v.x + x_p1), "{:.10f}".format(v.y + y_p1))


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


def cgl_4_a():
    """凸法を求める問題 https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/all/CGL_4_A"""
    N = int(input())
    lst = [Vector2D(*list(map(int, input().split()))) for _ in range(N)]
    for v in Vector2D.find_convex(lst):
        print(v.x, v.y)


if __name__ == "__main__":
    cgl_4_a()
    # cgl_1_b()
    # cgl_1_a()
    # cgl_2_a()
    # abc259_b()
    pass


