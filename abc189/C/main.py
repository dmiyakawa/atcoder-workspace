#!/usr/bin/env python3
from collections import Counter


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    solve2(N, A)


def solve2(N, A):
    # O(N) 解法。極大長方形
    # http://algorithms.blog55.fc2.com/blog-entry-132.html
    # https://atcoder.jp/contests/abc189/submissions/33058989
    stack = []
    max_sum = 0
    for i, a in enumerate(A):
        if stack:
            top = stack[-1]
            if top[1] < a:
                stack.append((i, a))
            elif top[1] > a:
                while stack and stack[-1][1] >= a:
                    top = stack.pop()
                    max_sum = max(max_sum, top[1] * (i - top[0]))
                stack.append((top[0], a))
        else:
            stack.append((i, a))
    while stack:
        top = stack.pop()
        max_sum = max(max_sum, top[1] * (N - top[0]))
    print(max_sum)


def solve1(N, A):
    # O(N^2) 解法
    # https://atcoder.jp/contests/abc189/submissions/33058797
    c = Counter(A)
    max_sum = 0
    for val in c.keys():
        cur_sum = 0
        for a in A:
            if a < val:
                max_sum = max(max_sum, cur_sum)
                cur_sum = 0
            else:
                cur_sum += val
        max_sum = max(max_sum, cur_sum)
    print(max_sum)


if __name__ == "__main__":
    main()
