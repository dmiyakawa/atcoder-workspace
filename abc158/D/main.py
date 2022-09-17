#!/usr/bin/env python3
from collections import deque


def main():
    import sys
    input = sys.stdin.readline

    deq = deque(input().rstrip())
    flipped = False
    Q = int(input())
    for _ in range(Q):
        query = input().rstrip().split()
        op = int(query[0])
        if op == 1:
            flipped = not flipped
        else:
            assert op == 2
            f = int(query[1])
            ch = query[2]
            if (not flipped and f == 1) or (flipped and f == 2):
                deq.appendleft(ch)
            else:
                deq.append(ch)
    if flipped:
        lst = reversed(deq)
    else:
        lst = list(deq)
    print("".join(lst))


if __name__ == "__main__":
    main()
