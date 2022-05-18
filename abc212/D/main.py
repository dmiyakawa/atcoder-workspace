#!/usr/bin/env python3

import heapq


def main():
    Q = int(input())
    queries = [tuple(int(e) for e in input().split()) for _ in range(Q)]
    hq = []
    offset = 0
    for query in queries:
        if query[0] == 1:
            heapq.heappush(hq, query[1] - offset)
        elif query[0] == 2:
            offset += query[1]
        else:
            value = heapq.heappop(hq)
            print(value + offset)


if __name__ == "__main__":
    main()
