#!/usr/bin/env python3

def main():
    N = int(input())
    lst = []
    for i in range(1, N + 1):
        s, p = [e for e in input().split()]
        lst.append((s, -int(p), i))
    lst.sort()
    for _, _, i in lst:
        print(i)


if __name__ == "__main__":
    main()
