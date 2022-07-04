#!/usr/bin/env python3

import sys


def gen(lst_rev):
    v = 0
    none_exists = False
    for i, n in enumerate(lst_rev):
        if n is None:
            none_exists = True
            for m in range(10):
                yield from gen([(m if j == i else val) for j, val in enumerate(lst_rev)])
        else:
            v += n * 10 ** i
    if not none_exists:
        yield v


def solve(N: int, M: int, S: "List[int]", C: "List[int]") -> int:
    lst = [None for _ in range(N)]
    for s, c in zip(S, C):
        s -= 1
        if lst[s] is None:
            lst[s] = c
        elif lst[s] != c:
            return -1

    for v in gen(list(reversed(lst))):
        if len(str(v)) == N:
            return v

    return -1


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    print(solve(N, M, s, c))


if __name__ == "__main__":
    main()
