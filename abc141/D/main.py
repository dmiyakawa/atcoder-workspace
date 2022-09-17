#!/usr/bin/env python3


def solve(N: int, M: int, A: "List[int]"):
    import heapq
    lst = []
    for a in A:
        heapq.heappush(lst, -a)
    for _ in range(M):
        a = -heapq.heappop(lst)
        a //= 2
        heapq.heappush(lst, -a)
    print(-sum(lst))


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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
