#!/usr/bin/env python3
import heapq


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    lst = [[] for _ in range(M + 1)]
    for a, b in zip(A, B):
        if a <= M:
            lst[a].append(b)
    hq = []
    ans = 0
    for m in range(1, M + 1):
        for b in lst[m]:
            heapq.heappush(hq, -b)
        if hq:
            ans += -heapq.heappop(hq)

    print(ans)


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
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == "__main__":
    main()
