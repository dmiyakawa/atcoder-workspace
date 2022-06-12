#!/usr/bin/env python3

def main():
    N = int(input())
    count = 0
    for _ in range(N):
        A, B = [int(e) for e in input().split()]
        C = B - A
        C = (C % 500) % 100
        count += C // 50
        C = (C % 50) % 10
        count += C // 5
    print(count)


if __name__ == "__main__":
    main()
