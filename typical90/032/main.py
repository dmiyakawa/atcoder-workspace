#!/usr/bin/env python3
#
# 感想:
# N! = 10! が十分小さいのでpermutationを全部舐めてもOKだった……
#

from typing import Dict, Set

MAX_VALUE = 1000 ** 10 + 1


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, A, M, X, Y)


def solve(N: int, A: "List[List[int]]", M: int, X: "List[int]", Y: "List[int]"):
    # n区までn名（最後は1<=j<=N)で走った際の時間の最小値
    ok_combinations: Dict[int, Set[int]] = {}
    for i in range(N):

        for j in range(N):
            ok_combinations.setdefault(i, set()).add(j)
    for x, y in zip(X, Y):
        ok_combinations[x - 1].remove(y - 1)
        ok_combinations[y - 1].remove(x - 1)

    dp = {(frozenset({i}), i): A[i][0] for i in range(N)}
    for i in range(1, N):
        current_items = list(dp.items())
        for (consumed, last), current_cost in current_items:
            available = ok_combinations[last] - consumed

            for next_last in available:
                next_consumed = frozenset(consumed.union({next_last}))
                dp[(next_consumed, next_last)] = min(dp.get((next_consumed, next_last), MAX_VALUE),
                                                     current_cost + A[next_last][i])
            del dp[(consumed, last)]

    # print(dp)
    values = dp.values()
    print(min(dp.values()) if values else -1, end="")


if __name__ == "__main__":
    main()
