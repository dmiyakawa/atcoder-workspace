#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    A_sum = sum(A)
    dp = [[(A.count(1), A.count(2), A.count(3), 0)]]
    for i in range(A_sum):
        lst = []
        for tup in dp[i]:
            m = sum(tup[:3])
            if m == N:
                r = 1
            else:
                r = N / (N - m)
            if tup[0]:
                lst.append((tup[0] - 1, tup[1], tup[2], tup[3] + r * tup[0] / m))
            if tup[1]:
                lst.append((tup[0] + 1, tup[1] - 1, tup[2], tup[3] + r * tup[1] / m))
            if tup[2]:
                lst.append((tup[0], tup[1] + 1, tup[2] - 1, tup[3] + r * tup[2] / m))
        dp.append(lst)
    print(sum(tup[3] for tup in dp[A_sum]))


if __name__ == "__main__":
    main()

