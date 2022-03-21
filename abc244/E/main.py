#!/usr/bin/env python3
from typing import Dict, Set

MOD = 998244353  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    U = [int()] * (M)  # type: "List[int]"
    V = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, M, K, S, T, X, U, V)


def solve(N: int, M: int, K: int, S: int, T: int, X: int, U: "List[int]", V: "List[int]"):
    # Sから始まりTでゴールするK個のノードからなる長さK+1の数列A[0]〜A[K], A[0] = S, A[K] = T
    # X (X != S, X != T が偶数回出現する)
    links: Dict[int, Set[int]] = {}
    for u, v in zip(U, V):
        links.setdefault(u, set()).add(v)
        links.setdefault(v, set()).add(u)

    possible_points = {S: {0: 1}}
    for i in range(K):
        next_possible_points = {}
        # dest_node に向かう場合
        for dest_node in range(1, N + 1):
            for src_node in links.get(dest_node, set()):
                x_incr = 1 if dest_node == X else 0
                x_count, count = possible_points.get(src_node, {})

        for current_p, x_to_count_d in possible_points.items():
            for next_node in links.get(current_p, set()):
                next_x_to_count_d = next_possible_points.setdefault(next_node, {})
                x_incr = 1 if next_node == X else 0
                for num_x, count in x_to_count_d.items():
                    next_x_to_count_d[num_x + x_incr] = \
                        (next_x_to_count_d.get(num_x + x_incr, 0) + count) % MOD
        possible_points = next_possible_points

    total_count = 0
    d = possible_points.get(T, {})

    for num_x_visits, count in d.items():
        if num_x_visits % 2 == 0:
            total_count += count
    print(total_count % MOD, end="")


if __name__ == "__main__":
    main()
