#!/usr/bin/env python
#
# https://atcoder.jp/contests/past202112-open/tasks/past202112_m
#

class Treap:
    """Treap implementation based on https://gist.github.com/irachex/3922705"""

    class Node:
        def __init__(self, key, data):
            import random
            self.key = key
            self.ran = random.random()
            self.size = 1
            self.cnt = 1
            self.data = data
            self.left = None
            self.right = None

        def left_rotate(self):
            a = self
            b = a.right
            a.right = b.left
            b.left = a
            a = b
            b = a.left
            b.size = b.left_size() + b.right_size() + b.cnt
            a.size = a.left_size() + a.right_size() + a.cnt
            return a

        def right_rotate(self):
            a = self
            b = a.left
            a.left = b.right
            b.right = a
            a = b
            b = a.right
            b.size = b.left_size() + b.right_size() + b.cnt
            a.size = a.left_size() + a.right_size() + a.cnt
            return a

        def left_size(self):
            return 0 if self.left is None else self.left.size

        def right_size(self):
            return 0 if self.right is None else self.right.size

        def __repr__(self):
            return '<node key:%s ran:%f size:%d left:%s right:%s>' % (
                str(self.key), self.ran, self.size, str(self.left), str(self.right))

    def __init__(self):
        self.root = None

    def _insert(self, node, key, data=None):
        if node is None:
            node = self.Node(key, data)
            return node
        node.size += 1
        if key < node.key:
            node.left = self._insert(node.left, key, data)
            if node.left.ran < node.ran:
                node = node.right_rotate()
        elif key >= node.key:
            node.right = self._insert(node.right, key, data)
            if node.right.ran < node.ran:
                node = node.left_rotate()
        else:
            # node.cnt += 1
            raise RuntimeError("It is not supported yet to insert identical objects multiple times")
        return node

    def insert(self, key, data=None):
        self.root = self._insert(self.root, key, data)

    def _find(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def find(self, key):
        return self._find(self.root, key)

    def _discard_inter(self, node, key):
        if node is None:
            return False
        if node.key == key:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                if node.left.ran < node.right.ran:
                    node = node.right_rotate()
                    node.right = self._discard_inter(node.right, key)
                else:
                    node = node.left_rotate()
                    node.left = self._discard_inter(node.left, key)
        elif key < node.key:
            node.left = self._discard_inter(node.left, key)
        else:
            node.right = self._discard_inter(node.right, key)
        node.size = node.left_size() + node.right_size() + node.cnt
        return node

    def discard(self, key) -> bool:
        if self.find(key) is None:
            return False
        self.root = self._discard_inter(self.root, key)
        return True

    def remove(self, key):
        if not self.discard(key):
            raise KeyError("Not found")

    def size(self):
        return 0 if self.root is None else self.root.size

    def median(self) -> int:
        s = self.size()
        if s == 0:
            return 0

        result: int
        if s % 2 == 1:
            result = self.find_kth(s / 2 + 1).key
        else:
            result = (self.find_kth(s / 2).key + self.find_kth(s / 2 + 1).key) / 2.0
        if result == int(result):
            result = int(result)
        return result

    def as_list(self):
        lst = []

        def _as_list_inter(node):
            if node is None:
                return
            _as_list_inter(node.left)
            lst.append(node.key)
            _as_list_inter(node.right)

        _as_list_inter(self.root)
        return lst

    def _find_kth(self, node, k):
        if node is None:
            return None
        if k <= node.left_size():
            return self._find_kth(node.left, k)
        if k > node.left_size() + node.cnt:
            return self._find_kth(node.right, k - node.left_size() - node.cnt)
        return node

    def find_kth(self, k):
        if k <= 0 or k > self.size():
            return None
        return self._find_kth(self.root, k)

    def __getitem__(self, i):
        """Returns i-th element of the tree"""
        if i < 0 or self.size() <= i:
            raise IndexError("index out of range")
        return self.find_kth(i + 1).key

    def __repr__(self):
        return str(self.root)


def main():
    N, Q = map(int, input().split())
    S = [e for e in input().split()]
    queries = []
    for _ in range(Q):
        query = input().split()
        queries.append((int(query[0]), query[1]))

    treap = Treap()
    for i, s in enumerate(S):
        treap.insert((s, i))
    for x, t in queries:
        name, _id = treap[x - 1]
        treap.remove((name, _id))
        treap.insert((t, _id))
    print(*[name for name, _id in sorted(treap.as_list(), key=lambda tup: tup[1])])


if __name__ == "__main__":
    main()
