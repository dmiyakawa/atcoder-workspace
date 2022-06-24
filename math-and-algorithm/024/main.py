#!/usr/bin/env python3

def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        p, q = [int(e) for e in input().split()]
        ans += q / p
    print(ans)


if __name__ == "__main__":
    main()
