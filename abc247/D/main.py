#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def main():
    from collections import deque
    Q = int(input())
    queries = [[int(e) for e in input().split()] for _ in range(Q)]
    dc = deque()

    for query in queries:
        if query[0] == 1:
            x, c = query[1], query[2]
            dc.append(x)
            dc.append(c)
        else:
            count = 0
            num_balls = query[1]
            while num_balls > 0:
                x = dc.popleft()
                c = dc.popleft()
                if c > num_balls:
                    count += x * num_balls
                    new_c = c - num_balls
                    dc.appendleft(new_c)
                    dc.appendleft(x)
                    break
                else:
                    count += x * c
                    num_balls -= c
            print(count)


if __name__ == "__main__":
    main()
