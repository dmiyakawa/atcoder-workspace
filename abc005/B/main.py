#!/usr/bin/env python3

def main():
    N = int(input())
    newest = 200
    for _ in range(N):
        newest = min(newest, int(input()))
    print(newest)


if __name__ == "__main__":
    main()
