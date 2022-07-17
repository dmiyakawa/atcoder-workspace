#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))


def solve(N: int, K: int, A: "List[int]"):
    dp = []
    for k in range(K + 1):
        winnable = False
        for a in A:
            if k - a < 0:
                continue
            elif not dp[k - a]:
                winnable = True
                break
        dp.append(winnable)
    print("First" if dp[K] else "Second")


def solve_tle(N: int, K: int, A: "List[int]"):
    stack = [K]
    cache = {}
    while stack:
        # print(stack)
        k = stack[-1]
        if k in cache:
            stack.pop()
            continue
        winnable = None
        recalc = False
        for a in A:
            if k - a < 0:
                continue
            if k - a not in cache:
                stack.append(k - a)
                recalc = True
            elif not cache[k - a]:
                winnable = True
            elif winnable is None:
                winnable = False
        if winnable is None:
            winnable = False

        if recalc:
            continue
        stack.pop()
        cache[k] = winnable
    # print(cache)
    print("First" if cache[K] else "Second")


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
