#!/usr/bin/env python3

def main():
    N = int(input())
    dp = [0]
    m = 0
    while N:
        dp.append(dp[-1] * min(10, N) + 0 if m == 0 else 10 ** m)
        N //= 10
        m += 1
    print(dp[-1])


if __name__ == "__main__":
    main()
