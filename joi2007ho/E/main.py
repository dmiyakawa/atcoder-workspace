#!/usr/bin/env python3


def main():
    N = int(input())
    raw_bars = [tuple(map(int, input().split())) for _ in range(N)]
    parents = {i: -1 for i in range(N)}
    for i, b in enumerate(raw_bars):
        if b[2]:
            j = b[2] - 1
            assert parents[j] == -1
            parents[j] = i
        if b[3]:
            j = b[3] - 1
            assert parents[j] == -1
            parents[j] = i
    roots = [i for i, p in parents.items() if p == -1]
    assert len(roots) == 1

    def calc(parent_i):
        bar = raw_bars[parent_i]
        lw = calc(bar[2] - 1) if bar[2] else 1
        rw = calc(bar[3] - 1) if bar[3] else 1
        tmp = lcm(bar[0] * lw, bar[1] * rw)
        return tmp // bar[0] + tmp // bar[1]

    print(calc(roots[0]))


def lcm(a, b):
    import math
    return a // math.gcd(a, b) * b


if __name__ == "__main__":
    main()
