#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    zero_exists = False
    lst = []
    for _ in range(K):
        n = int(input())
        if n == 0:
            zero_exists = True
        else:
            lst.append(n)
    lst.sort()
    lst2 = []
    l = None
    for i, n in enumerate(lst):
        if i == 0:
            l = n
        elif lst[i - 1] + 1 < n:
            lst2.append((l, lst[i - 1]))
            l = n
    lst2.append((l, lst[-1]))
    ans = 0
    # print(lst2, zero_exists)
    for i in range(len(lst2)):
        ans = max(ans, lst2[i][1] - lst2[i][0] + 1)
        if zero_exists and i < len(lst2) - 1 and lst2[i][1] + 2 == lst2[i + 1][0]:
            ans = max(ans, lst2[i + 1][1] - lst2[i][0] + 1)
    print(ans)


if __name__ == "__main__":
    main()
