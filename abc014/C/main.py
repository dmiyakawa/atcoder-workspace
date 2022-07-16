#!/usr/bin/env python3

import sys

def solve(N: int, A: "List[int]", B: "List[int]"):
    C = []
    for a in A:
        C.append((a, 1))
    for b in B:
        C.append((b + 1, -1))
    C.sort()
    max_num = 0
    num = 0
    for i, u in C:
        num += u
        max_num = max(max_num, num)
    print(max_num)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int()] * (n)  # type: "List[int]"
    b = [int()] * (n)  # type: "List[int]"
    for i in range(n):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(n, a, b)


if __name__ == "__main__":
    main()
