#!/usr/bin/env python3


def main():
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    # solve(N, X)
    solve2(N, X)


def solve2(N, X):
    pos_to_node = [i for i in range(N)]
    node_to_pos = [i for i in range(N)]
    for node in X:
        node -= 1
        pos = node_to_pos[node]
        if pos < N - 1:
            right = pos_to_node[pos + 1]
            node_to_pos[right] = pos
            node_to_pos[node] = pos + 1
            pos_to_node[pos + 1] = node
            pos_to_node[pos] = right
        else:
            left = pos_to_node[pos - 1]
            node_to_pos[left] = pos
            node_to_pos[node] = pos - 1
            pos_to_node[pos - 1] = node
            pos_to_node[pos] = left
    print(*[node + 1 for node in pos_to_node])


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve(N, X):
    nodes = [Node(i) for i in range(1, N + 1)]
    for i, node in enumerate(nodes):
        if i > 0:
            left = nodes[i - 1]
            left.right = node
            node.left = left
        if i < N - 1:
            right = nodes[i + 1]
            right.left = node
            node.right = right
    head = nodes[0]

    for x in X:
        x -= 1
        node = nodes[x]
        if node.right is not None:
            right = node.right

            if node.left is not None:
                left = node.left
                left.right = right
            else:
                left = None
                head = right


            if right.right is not None:
                right.right.left = node
            node.right = right.right
            right.right = node

            node.left = right
            right.left = left
        else:
            left = node.left
            if left.left is not None:
                left.left.right = node
            else:
                head = node

            node.right = left
            left.right = None
            node.left = left.left
            left.left = node

    node = head
    lst = []
    while node:
        lst.append(node.val)
        node = node.right
    print(*lst)


def _debug():
    import random
    N = 2 * 10**5
    X = [random.randint(1, N) for _ in range(random.randint(1, 2 * 10**5))]
    solve(N, X)


if __name__ == "__main__":
    # _debug()
    main()
