#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]

    m = (N - 1) // 2
    lst = [0] * N
    prev_ans = None
    for i in range(N):
        if i == 0:
            ans = 0
            for j in range(m + 1):
                ans += A[2 * j]
            for j in range(m):
                ans -= A[2 * j + 1]
        else:
            ans = prev_ans - 2 * A[(2 * i - 2) % N] + 2 * A[(2 * i - 1) % N]
        lst[i * 2 % N] = ans
        prev_ans = ans
    print(*lst)


if __name__ == "__main__":
    main()
