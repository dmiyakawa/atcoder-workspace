#!/usr/bin/env python3


import math

cache = {}


def sqrt(x):
    xx = int(math.sqrt(x) // 1)
    ans = 0
    for i in range(-1, 2):
        tmp = xx + i
        if tmp >= 0:
            if tmp * tmp <= x:
                ans = tmp
    return ans


def flsq(x):
    if x == 1:
        return 1
    if x in cache:
        return cache[x]
    floored = int(sqrt(x))
    ret = (x - floored ** 2 + 1) * flsq(floored)
    for i in range(floored - 1, 0, -1):
        ret += ((i + 1) ** 2 - i ** 2) * flsq(i)
    cache[x] = ret
    return ret


def count(x):
    if x == 1:
        return 1
    val = int(sqrt(x))
    if val == 1:
        return 1
    return flsq(val)


def calc(T, X):
    ans = []
    for i in range(T):
        ans.append(count(X[i]))
    return ans


def main():
    T = int(input())
    X = []
    for _ in range(T):
        X.append(int(input()))
    print(*calc(T, X), sep="\n")


if __name__ == "__main__":
    main()
