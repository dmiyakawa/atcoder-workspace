#!/usr/bin/env python3

class Node:
    def __init__(self, n):
        self.n = n
        self.prev = None
        self.next = None


def main():
    N, Q = map(int, input().split())
    d = {n: Node(n) for n in range(1, N + 1)}

    for _ in range(Q):
        query = list(map(int, input().split()))
        op = query[0]
        if op == 1:
            x, y = query[1:]
            d[x].next = d[y]
            d[y].prev = d[x]
        elif op == 2:
            x, y = query[1:]
            d[x].next = None
            d[y].prev = None
        else:
            x = query[1]
            node = d[x]
            while node.prev:
                node = node.prev
            lst = []
            while node:
                lst.append(node.n)
                node = node.next
            print(len(lst), *lst)


if __name__ == "__main__":
    main()
