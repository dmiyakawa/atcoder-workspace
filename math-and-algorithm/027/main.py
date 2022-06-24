#!/usr/bin/env python3

from typing import List


def my_sort(lst: List[int]):
    if len(lst) == 1:
        return lst.copy()
    n = len(lst) // 2
    a = my_sort(lst[:n])
    b = my_sort(lst[n:])
    ai = 0
    bi = 0
    ret = []
    while ai < len(a) or bi < len(b):
        if ai == len(a):
            ret.append(b[bi])
            bi += 1
        elif bi == len(b):
            ret.append(a[ai])
            ai += 1
        elif a[ai] < b[bi]:
            ret.append(a[ai])
            ai += 1
        else:
            ret.append(b[bi])
            bi += 1
    return ret


def main():
    input()
    print(*my_sort(list(map(int, input().split()))))


if __name__ == "__main__":
    main()
