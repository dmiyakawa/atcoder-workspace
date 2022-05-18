#!/usr/bin/env python3

def main():
    N = int(input())
    ans = 0
    for n in range(1, N + 1):
        ans += 1/N * n * 10000
    print(ans)


if __name__ == "__main__":
    main()
