#!/usr/bin/env python3

def main():
    H, W = [int(e) for e in input().split()]
    R, C = [int(e) for e in input().split()]
    solve(H, W, R, C)


def solve(H: int, W: int, R: int, C: int):
    count = 0
    if R > 1:
        count += 1
    if R < H:
        count += 1
    if C > 1:
        count += 1
    if C < W:
        count += 1
    print(count)


if __name__ == "__main__":
    main()
