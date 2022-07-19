#!/usr/bin/env python3

import sys

def main2():
    # 回答例を見てから
    N, C = map(int, input().split())
    lst = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        a -= 1
        lst.append((a, c))
        lst.append((b, -c))
    lst.sort()
    total = 0
    d = 0
    fee = 0
    for d0, c in lst:
        if d0 != d:
            total += min(C, fee) * (d0 - d)
            d = d0
        fee += c
    print(total)


def solve(N: int, C: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    D = []
    for a0, c0 in zip(a, c):
        D.append((a0, c0))
    for b0, c0 in zip(b, c):
        D.append((b0 + 1, -c0))
    D.sort()
    E = []
    a1 = None
    c1 = 0
    for tup in D:
        if a1 == tup[0]:
            c1 += tup[1]
        else:
            if a1 is not None:
                E.append((a1, c1))
            a1 = tup[0]
            c1 += tup[1]
    if a1 is not None:
        E.append((a1, c1))
    a2 = None
    c2 = None
    total = 0
    # print(E)
    for tup in E:
        if a2 is not None:
            total += (tup[0] - a2) * min(c2, C)
        a2, c2 = tup
    print(total)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, a, b, c)


if __name__ == "__main__":
    main2()
