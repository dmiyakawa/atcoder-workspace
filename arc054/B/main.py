#!/usr/bin/env python3

import math


def main():
    P = float(input())

    def _func(_t):
        return _t + P * math.pow(0.5, _t/1.5)

    lb = 0
    ub = 10 ** 18
    for i in range(200):
        t1 = (2 * lb + ub) / 3
        t2 = (lb + 2 * ub) * 2 / 3
        b = _func(t1)
        c = _func(t2)
        if b < c:
            ub = t2
        else:
            lb = t1
    print(lb)


if __name__ == "__main__":
    main()
