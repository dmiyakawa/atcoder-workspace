#!/usr/bin/env python3
import heapq
import sys
from collections import deque

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    Q = int(input())
    hq = []
    dq = deque()
    for _ in range(Q):
        query = input().split()
        op = int(query[0])
        if op == 1:
            dq.append(int(query[1]))
        elif op == 2:
            if hq:
                v = heapq.heappop(hq)
            else:
                v = dq.popleft()
            print(v)
        else:
            assert op == 3
            while dq:
                heapq.heappush(hq, dq.popleft())


if __name__ == "__main__":
    main()
