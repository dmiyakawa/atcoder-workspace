#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (M)  # type: "List[int]"
    D = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    print(YES if solve(N, M, A, B, C, D) else NO)


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    import itertools
    lst1 = sorted(zip(A, B))
    for mapping in itertools.permutations([i for i in range(1, N + 1)]):
        lst2 = []
        for co, do in zip(C, D):
            cc = mapping[co - 1]
            dc = mapping[do - 1]
            lst2.append((min(cc, dc), max(cc, dc)))
        lst2.sort()
        if lst1 == lst2:
            return True
    return False


if __name__ == "__main__":
    main()
