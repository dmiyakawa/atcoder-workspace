#!/usr/bin/env python3

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    max_m = -10**19
    b = 0
    for i, a in enumerate(A):
        b += a
        max_m = max(max_m, b)
        B.append((max_m, b))

    ans = 0
    c = 0
    for b in B:
        ans = max(ans, c + b[0])
        c += b[1]
    print(ans)


if __name__ == "__main__":
    main()
