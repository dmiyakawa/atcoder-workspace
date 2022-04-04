#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


def solve(N: int, A: "List[int]"):
    unmatched = {}
    for i in range(N//2):
        if A[i] == A[N - 1 - i]:
            continue
        s = min(A[i], A[N - 1 - i])
        l = max(A[i], A[N - 1 - i])
        unmatched.setdefault(s, set()).add(l)
        unmatched.setdefault(l, set()).add(s)

    unused = set(unmatched.keys())
    count = 0
    while unused:
        node1 = unused.pop()
        linked = {node1}
        to_visit = {node1}
        while to_visit:
            node = to_visit.pop()
            for l_node in unmatched[node]:
                unused.discard(l_node)
                if l_node not in linked:
                    linked.add(l_node)
                    to_visit.add(l_node)
        count += len(linked) - 1
    print(count)


if __name__ == "__main__":
    main()
