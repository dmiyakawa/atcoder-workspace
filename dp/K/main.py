#!/usr/bin/env python3

import sys


def solve(N: int, K: int, A: "List[int]"):
    As = set(A)
    Bs = set()
    for a in A:
        for b in A:
            Bs.add(a + b)
    Cs = Bs - As
    dp = {a: 0 for a in A}
    
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)





if __name__ == "__main__":
    main()
