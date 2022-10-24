#!/usr/bin/env python3

class Node:
    def __init__(self, n, parent):
        self.n = n
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0


def solve(N: int, A: "List[int]"):
    d = {1: Node(1, None)}
    for i, a in enumerate(A, start=1):
        d[2 * i] = Node(2 * i, d[a])
        d[2 * i + 1] = Node(2 * i + 1, d[a])
    for i in range(1, 2 * N + 2):
        print(d[i].depth)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
