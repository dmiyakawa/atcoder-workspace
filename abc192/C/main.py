#!/usr/bin/env python3

def main():
    N, K = [int(e) for e in input().split()]
    n = N
    for k in range(K):
        lst = []
        while n:
            lst.append(n % 10)
            n = n // 10
        g1, g2 = 0, 0
        for val in sorted(lst, reverse=True):
            g1 = g1 * 10 + val
        for val in sorted(lst):
            g2 = g2 * 10 + val
        n = g1 - g2
        if n == 0:
            break
    print(n)


if __name__ == "__main__":
    main()
