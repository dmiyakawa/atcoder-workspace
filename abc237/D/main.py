#!/usr/bin/env python3

import sys

class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<{self.n}, {self.left.n if self.left else None}, {self.right.n if self.right else None}>"


def solve(N: int, S: str):
    root = Node(0)
    node = root
    for i in range(1, N + 1):
        new_node: Node
        if S[i - 1] == "L":
            new_node = Node(i)
            node.left = new_node
        else:
            new_node = Node(i)
            node.right = new_node
        node = new_node
    stack = [root]
    lst = []
    while stack:
        node = stack[-1]
        # print(node.n, node.left, node.right, stack)
        if node.left:
            stack.append(node.left)
            node.left = None
            continue
        node = stack.pop()
        lst.append(node.n)
        if node.right:
            stack.append(node.right)
    print(*lst)


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == "__main__":
    main()
