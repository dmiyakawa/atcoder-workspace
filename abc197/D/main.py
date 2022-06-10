#!/usr/bin/env python3

def main():
    import math
    N = int(input())
    rad = 2 * math.pi / N
    x0, y0 = [int(e) for e in input().split()]
    xn2, yn2 = [int(e) for e in input().split()]
    xc, yc = (x0 + xn2) / 2, (y0 + yn2) / 2
    vx, vy = xc - x0, yc - y0
    l = math.sqrt(vx**2 + vy**2)
    ux, uy = vx / l, vy / l
    rad2 = rad * (N // 2 - 1)
    rux = ux * math.cos(-rad2) - uy * math.sin(-rad2)
    ruy = ux * math.sin(-rad2) + uy * math.cos(-rad2)
    rx, ry = rux * l, ruy * l
    # print(f"rx: {rx}, ry: {ry}")
    ax, ay = x0 + vx + rx, y0 + vy + ry
    print(ax, ay)


if __name__ == "__main__":
    main()
