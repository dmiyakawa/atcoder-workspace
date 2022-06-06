#!/usr/bin/env python3


def main():
    H, W = [int(e) for e in input().split()]
    grid = [[e for e in input().split()] for _ in range(H)]
    print(H, W)
    print(grid)


if __name__ == "__main__":
    main()
