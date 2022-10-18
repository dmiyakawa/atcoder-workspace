#!/usr/bin/env python3
from typing import Optional


class Node:
    def __init__(self, n, prev=None):
        self.n = n
        self.prev = prev


def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    d = {}
    node: Optional[Node] = None
    ans = []
    for i in range(Q):
        query = input().rstrip().split()
        # print(i, query)
        op = query[0]
        if op == "ADD":
            x = int(query[1])
            if node:
                prev = node
                node = Node(x, prev)
            else:
                node = Node(x)
        elif op == "DELETE":
            if node:
                node = node.prev
        elif op == "SAVE":
            y = int(query[1])
            d[y] = node
        else:
            assert op == "LOAD"
            z = int(query[1])
            node = d.get(z, None)
        if node:
            ans.append(node.n)
        else:
            ans.append(-1)
    print(*ans)


if __name__ == "__main__":
    main()
