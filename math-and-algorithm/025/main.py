#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    total = 0
    for i in range(N):
        total += A[i] * 2 / 6 + B[i] * 4 / 6
    print(total)


if __name__ == "__main__":
    main()
