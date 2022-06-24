#!/usr/bin/env python3


def main():
    T = int(input())
    N = int(input())
    lst = [0 for _ in range(T + 1)]
    for _ in range(N):
        l, r = map(int, input().split())
        lst[l] += 1
        lst[r] -= 1
    count = 0
    for t in range(T):
        count += lst[t]
        print(count)


if __name__ == "__main__":
    main()
