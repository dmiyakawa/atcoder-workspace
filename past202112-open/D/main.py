#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    lst = sorted(((a, b, i) for i, (a, b) in enumerate(zip(A, B), start=1)),
                 reverse=True,
                 key=lambda tup: (tup[0] + tup[1], tup[0], -tup[2]))
    print(*[i for a, b, i in lst[:N]])


if __name__ == "__main__":
    main()
