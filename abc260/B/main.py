#!/usr/bin/env python3

import sys

def solve2(N: int, X: int, Y: int, Z: int, A: "List[int]", B: "List[int]"):
    passed = [False for _ in range(N + 1)]
    C = []
    for i, (a, b) in enumerate(zip(A, B), start=1):
        C.append((-a, -b, i))
    C.sort(key=lambda tup: (tup[0], tup[2]))
    x = X
    for i, c in enumerate(C):
        if x == 0:
            break
        if not passed[c[2]]:
            passed[c[2]] = True
            x -= 1
    C.sort(key=lambda tup: (tup[1], tup[2]))
    y = Y
    for i, c in enumerate(C):
        if y == 0:
            break
        if not passed[c[2]]:
            passed[c[2]] = True
            y -= 1
    C.sort(key=lambda tup: (tup[0] + tup[1], tup[2]))
    z = Z
    for i, c in enumerate(C):
        if z == 0:
            break
        if not passed[c[2]]:
            passed[c[2]] = True
            z -= 1

    for i, p in enumerate(passed):
        if p:
            print(i)


def solve(N: int, X: int, Y: int, Z: int, A: "List[int]", B: "List[int]"):
    # 本番解法
    C = []
    p = set()
    for n, (a, b) in enumerate(zip(A, B), start=1):
        C.append((a, b, n))

    rem = X
    # t[2]をkeyに入れるのが筋。ただ、安定ソートだったので運がよく通った
    for tup in sorted(C, key=lambda t: -t[0]):
        if rem == 0:
            break
        if tup not in p:
            p.add(tup)
            rem -= 1
    rem = Y
    for tup in sorted(C, key=lambda t: -t[1]):
        if rem == 0:
            break
        if tup not in p:
            p.add(tup)
            rem -= 1
    rem = Z
    for tup in sorted(C, key=lambda t: (-t[0] - t[1], t[2])):
        if rem == 0:
            break
        if tup not in p:
            p.add(tup)
            rem -= 1
    for tup in sorted(p, key=lambda t: t[2]):
        print(tup[2])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    # solve(N, X, Y, Z, A, B)
    solve2(N, X, Y, Z, A, B)


if __name__ == "__main__":
    main()
