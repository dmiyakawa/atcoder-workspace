#!/usr/bin/env python3

def main():
    N = int(input())
    ans = 1
    for n in range(1, N):
        ans += N / (N - n)
    print(ans)


if __name__ == "__main__":
    main()
