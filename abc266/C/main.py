#!/usr/bin/env python3
import math

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(A_x: int, A_y: int, B_x: int, B_y: int, C_x: int, C_y: int, D_x: int, D_y: int):
    pA = Point2D(A_x, A_y)
    pB = Point2D(B_x, B_y)
    pC = Point2D(C_x, C_y)
    pD = Point2D(D_x, D_y)
    print("Yes" if detect_intersection(pA, pC, pB, pD) else "No")


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


def solve_wa(A_x: int, A_y: int, B_x: int, B_y: int, C_x: int, C_y: int, D_x: int, D_y: int):

    def func(x1, y1, x2, y2, x3, y3):
        a = math.sqrt((x1**2 + y1**2) * (x2**2 + y2**2) - (x1*x2 + y1*y2)**2) / 2
        b = math.sqrt((x2**2 + y2**2) * (x3**2 + y3**2) - (x2*x3 + y2*y3)**2) / 2
        c = math.sqrt((x1**2 + y1**2) * (y3**2 + y3**2) - (x1*x3 + y1*y3)**2) / 2

        return a + b > c

    lst = [(A_x, A_y), (B_x, B_y), (C_x, C_y), (D_x, D_y)]
    for i in range(4):
        p1 = lst[i]
        p2 = lst[(i + 1) % 4]
        p3 = lst[(i + 2) % 4]
        p4 = lst[(i + 3) % 4]
        if not func(p2[0] - p1[0], p2[1] - p1[1],
                    p3[0] - p1[0], p3[1] - p1[1],
                    p4[0] - p1[0], p4[1] - p1[1]):
            print("No")
            return
    print("Yes")


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A_x = int(next(tokens))  # type: int
    A_y = int(next(tokens))  # type: int
    B_x = int(next(tokens))  # type: int
    B_y = int(next(tokens))  # type: int
    C_x = int(next(tokens))  # type: int
    C_y = int(next(tokens))  # type: int
    D_x = int(next(tokens))  # type: int
    D_y = int(next(tokens))  # type: int
    solve(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y)


if __name__ == "__main__":
    main()
