#!/usr/bin/env python3


from bisect import bisect_left, bisect_right

MAX = 2*10**5 + 1


def main2():
    # https://atcoder.jp/contests/abc256/editorial/4121
    N = int(input())
    lst = []
    for _ in range(N):
        l, r = [int(e) for e in input().split()]
        lst.append((l, 1))
        lst.append((r, -1))
    lst.sort(key=lambda tup: (tup[0], -tup[1]))
    d = {}
    count = 0
    for t, s in lst:
        count += s
        d[t] = count
    left = 0
    ans = []
    prev = 0
    for t, s in sorted(d.items()):
        if prev == 0 and s > 0:
            left = t
        elif s == 0 and prev > 0:
            ans.append((left, t))
        prev = s
    for l, r in ans:
        print(l, r)


def main():
    N = int(input())
    lst = []
    for _ in range(N):
        l, r = [int(e) for e in input().split()]
        lst.append((l, r))
    lst.sort()
    left = 0
    right = 0
    new_ranges = []
    while True:
        left_index = bisect_left(lst, (left, right))
        if left_index >= len(lst):
            break
        left, right = lst[left_index]
        while True:
            i = bisect_right(lst, (right, MAX))
            if left_index >= i:
                new_ranges.append((left, right))
                left = right
                right = MAX
                break
            for j in range(left_index, i):
                tup = lst[j]
                right = max(right, tup[1])
            left_index = i
    for l, r in sorted(new_ranges):
        print(l, r)


if __name__ == "__main__":
    main2()
