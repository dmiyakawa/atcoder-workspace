#!/usr/bin/env python3

def main():
    n, X = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    i = 0
    total = 0
    while X:
        if X % 2:
            total += A[i]
        X //= 2
        i += 1
    print(total)


if __name__ == "__main__":
    main()
