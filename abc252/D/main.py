#!/usr/bin/env python3
from collections import Counter


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    counter = Counter(A)
    A_max = max(A)
    lst = [0 for _ in range(A_max + 2)]
    for i in range(1, A_max + 2):
        lst[i] = lst[i - 1] + counter[i - 1]
    ans = 0
    for v, num in counter.items():
        if v == A_max:
            continue
        # print(len(lst), A_max + 1, v + 1)
        ans += num * lst[v] * (lst[A_max + 1] - lst[v + 1])

    print(ans)


if __name__ == "__main__":
    main()
