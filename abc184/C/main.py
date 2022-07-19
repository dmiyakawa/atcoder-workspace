#!/usr/bin/env python3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1, c1) == (r2, c2):
        return 0
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    elif abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3 or (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 5:
        return 2
    else:
        return 3


if __name__ == "__main__":
    print(main())
