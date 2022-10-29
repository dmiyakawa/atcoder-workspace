#!/usr/bin/env python3



def solve(N: int, A: "List[str]", B: "List[str]"):
    print(topological_sort_kahn_pqueue(2, []))


def topological_sort_kahn_pqueue(N, E: "Collection[Tuple[int, int]]") -> "Optional[Tuple[List[int], bool]]":
    """「Kahnのアルゴリズム」でheapqを適用したもの。辞書順になる"""
    import heapq
    from typing import List

    G: List[List[int]] = [[] for _ in range(N)]
    C = [0] * N

    for i, j in E:
        G[i] += j,
        C[j] += 1

    hq = []
    for i in range(N):
        if C[i]:
            continue
        heapq.heappush(hq, i)

    is_unique = True
    ans = []
    while hq:
        if 1 < len(hq):
            is_unique = False
        i = heapq.heappop(hq)
        ans.append(i)
        for j in G[i]:
            C[j] -= 1
            if not C[j]:
                heapq.heappush(hq, j)
    if sum(C) > 0:
        return None
    else:
        return ans, is_unique


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [str()] * (N)  # type: "List[str]"
    B = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        A[i] = next(tokens)
        B[i] = next(tokens)
    solve(N, A, B)


if __name__ == "__main__":
    main()
