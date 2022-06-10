#!/usr/bin/env python3

def main():
    N = int(input())
    P = [float(e) for e in input().split()]
    dp = [[1 if i == 0 else 0 for i in range(N + 1)]]
    for i in range(N):
        prev_lst = dp[-1]
        lst = [0 for _ in range(N + 1)]
        dp.append(lst)
        for j in range(N):
            lst[j] += prev_lst[j] * (1 - P[i])
            lst[j + 1] += prev_lst[j] * P[i]

    print(sum(dp[-1][i] for i in range(N + 1) if i * 2 > N))


if __name__ == "__main__":
    main()
