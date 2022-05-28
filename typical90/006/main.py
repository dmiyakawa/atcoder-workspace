#!/usr/bin/env python3

Inf = float("Inf")


def solve_ref(N: int, K: int, S: str):
    # 解説に基づく実装
    # https://twitter.com/e869120/status/1379202843622576130/photo/1
    # https://github.com/E869120/kyopro_educational_90/blob/main/sol/006.cpp
    nex = []
    for _ in range(26):
        nex.append([len(S)] * (N + 1))

    for i in range(len(S) - 1, -1, -1):
        for j in range(26):
            if ord(S[i]) - ord("a") == j:
                nex[j][i] = i
            else:
                nex[j][i] = nex[j][i + 1]

    ans = []
    cur_pos = 0
    for i in range(1, K + 1):
        for j in range(26):
            nex_pos = nex[j][cur_pos]
            max_possible_length = len(S) - nex_pos - 1 + i
            if max_possible_length >= K:
                ans.append(chr(j + ord("a")))
                cur_pos = nex_pos + 1
                break
    print("".join(ans))


#
# ACは出ているが解説の解法と違うもの
# Linked Listで文字をノードとして持ちつつ、辞書順で「反転」しているノードを先頭から記録しておき、
# K文字を越したら反転している部分をLinked Listから捨て、
# 新たに隣接したノードについて「反転」を確認し、必要ならリストの先頭に改めて挿入する
#
class Node:
    def __init__(self, ch, prev_node, next_node):
        self.ch = ch
        self.prev = prev_node
        self.next = next_node

    def to_str(self):
        lst = []
        node = self
        while node is not None:
            lst.append(node.ch)
            node = node.next
        return "".join(lst)


def solve(N: int, K: int, S: str):
    head: "Node"
    tail: "Node"
    reversed_nodes = []
    for i, ch in enumerate(S):
        node = Node(ch, None, None)
        if i == 0:
            head = tail = node
            continue

        tail.next = node
        node.prev = tail
        if tail.ch > node.ch:
            reversed_nodes.append(tail)
        tail = node
        if i >= K:
            if reversed_nodes:
                reversed_node = reversed_nodes.pop(0)
                if reversed_node is head:
                    head = head.next
                    head.prev = None
                else:
                    prev_node = reversed_node.prev
                    next_node = reversed_node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    if prev_node.ch > next_node.ch:
                        reversed_nodes.insert(0, prev_node)
            else:
                tail = tail.prev
                tail.next = None

    print(head.to_str())


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve_ref(N, K, S)


if __name__ == "__main__":
    main()
