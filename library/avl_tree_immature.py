#!/usr/bin/env python3
#
# 平衡二分探索木。やや実践で使うには未成熟
# - 要素を削除できない
# - 同じ要素を2つ追加できない
#
# 元ネタ
# https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/avl_tree
#

import math
from collections import defaultdict


class AVLTree:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, value):
        self.root = self.Node(value)
        self.max_depth = 0
        self.total = 1
        self.nodes = defaultdict(list)

    def balance(self):
        return int(math.log2(self.total))

    def single_left_rotate(self, new_root):
        tmp = new_root.right
        new_root.right = self.root
        self.root.left = tmp
        self.root = new_root

    def double_left_rotate(self, new_root):
        tmp_left = new_root.left
        tmp_right = new_root.right
        new_root.left = self.root.left
        new_root.right = self.root
        self.root.left.right = tmp_left
        self.root.left = tmp_right
        self.root = new_root

    def single_right_rotate(self, new_root):
        tmp = new_root.left
        new_root.left = self.root
        self.root.right = tmp
        self.root = new_root

    def double_right_rotate(self, new_root):
        tmp_left = new_root.left
        tmp_right = new_root.right
        new_root.left = self.root
        new_root.right = self.root.right
        self.root.right.left = tmp_right
        self.root.right = tmp_left
        self.root = new_root

    def insert(self, value):
        node = self.root
        direction = None
        parent = None
        flag = None
        while node:
            parent = node
            if node.value == value:
                print("Data already exists.")
                return
            elif node.value > value:
                node = node.left
                flag = "left"
                if not direction:
                    direction = "left"
            else:
                node = node.right
                flag = "right"
                if not direction:
                    direction = "right"
        new = self.Node(value)

        assert parent is not None
        assert flag is not None

        if flag == "left":
            parent.left = new
        else:
            parent.right = new
        self.total += 1
        self.get_max_depth(self.root)
        if self.max_depth - self.balance() >= 1:
            if direction == "left":
                if self.root.left.value > value:
                    self.single_left_rotate(self.root.left)
                else:
                    self.double_left_rotate(self.root.left.right)
            else:
                if self.root.right.value < value:
                    self.single_right_rotate(self.root.right)
                else:
                    self.double_right_rotate(self.root.right.left)

    def get_max_depth(self, tree, depth=0):
        tmp = tree
        if tmp is None:
            depth -= 1
            if self.max_depth < depth:
                self.max_depth = depth
        else:
            self.get_max_depth(tmp.left, depth + 1)
            self.get_max_depth(tmp.right, depth + 1)

    def get_tree_structure(self, tree, depth):
        tmp = tree
        if tmp is None:
            return
        else:
            self.get_tree_structure(tmp.left, depth + 1)
            self.nodes[depth].append(tmp.value)
            self.get_tree_structure(tmp.right, depth + 1)

    def display(self):
        self.nodes = defaultdict(list)
        self.get_tree_structure(self.root, 0)
        depth = len(self.nodes)
        for d in range(depth):
            if d == 0:
                print("root   : ", end="")
            else:
                print("depth {}: ".format(d), end="")
            for node in self.nodes[d]:
                print("{0:3}".format(node), end=", ")
            print()

    def __iter__(self):
        def _next_inter(node):
            if node is None:
                return
            yield from _next_inter(node.left)
            yield node.value
            yield from _next_inter(node.right)

        yield from _next_inter(self.root)


def main():
    t = AVLTree(10)
    print("Inserting 5, 20, 13, 30")
    t.insert(5)
    t.insert(20)
    t.insert(13)
    t.insert(30)
    print([v for v in t])
    print("Insert 15")
    t.insert(15)
    print([v for v in t])


if __name__ == "__main__":
    main()
