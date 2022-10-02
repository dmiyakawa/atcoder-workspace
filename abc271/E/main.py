#!/usr/bin/env python3


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", E: "List[int]"):
    costs = {0: 0}
    for i, e in enumerate(E):
        e -= 1
        a, b = A[e] - 1, B[e] - 1
        if a in costs:
            costs[b] = min(costs[a] + C[e], costs.get(b, float("inf")))
    print(costs.get(N-1, -1))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    E = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, M, K, A, B, C, E)


if __name__ == "__main__":
    main()
