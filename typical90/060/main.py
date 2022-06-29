#!/usr/bin/env python3

from bisect import bisect_left

def main():
    N = int(input())
    A = [int(e) for e in input().split()]

    dp_l = []
    len_l = []
    for i, a in enumerate(A):
        j = bisect_left(dp_l, a)
        if j < len(dp_l):
            dp_l[j] = a
        else:
            dp_l.append(a)
        len_l.append(len(dp_l))

    A.reverse()
    dp_r = []
    len_r = []
    for i, a in enumerate(A):
        j = bisect_left(dp_r, a)
        if j < len(dp_r):
            dp_r[j] = a
        else:
            dp_r.append(a)
        len_r.append(len(dp_r))
    len_r.reverse()
    print(max(l + r - 1 for l, r in zip(len_l, len_r)))


if __name__ == "__main__":
    main()
