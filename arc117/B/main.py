#!/usr/bin/env python3

MOD = 10**9 + 7

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    lst = sorted(set(A), reverse=True)
    count = 1
    for i in range(1, len(lst) + 1):
        prev_n = lst[i - 1]
        cur_n = 0 if i == len(lst) else lst[i]
        # print(count, prev_n, cur_n, prev_n - cur_n)
        count = count * (prev_n - cur_n + 1) % MOD
    print(count)


if __name__ == "__main__":
    main()
