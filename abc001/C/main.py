#!/usr/bin/env python3

from decimal import *


def main():
    deg_10, dis_m = [Decimal(e) for e in input().split()]
    deg_100 = deg_10 * 10
    dis_s = (dis_m / 60).quantize(Decimal("1.0"), rounding=ROUND_HALF_UP)
    W = 12
    for i, val_s in enumerate(["0.2", "1.5", "3.3", "5.4", "7.9", "10.7", "13.8", "17.1",
                               "20.7", "24.4", "28.4", "32.6"]):
        if dis_s <= Decimal(val_s):
            W = i
            break
    if W == 0:
        dir_ = "C"
    else:
        dir_ = "N"
        for value, dir__ in [(1125, "N"), (3375, "NNE"), (5625, "NE"), (7875, "ENE"), (10125, "E"), (12375, "ESE"),
                             (14625, "SE"), (16875, "SSE"), (19125, "S"), (21375, "SSW"), (23625, "SW"),
                             (25875, "WSW"), (28125, "W"), (30375, "WNW"), (32625, "NW"), (34875, "NNW")]:
            if deg_100 < value:
                dir_ = dir__
                break

    print(dir_, W)


if __name__ == "__main__":
    main()
