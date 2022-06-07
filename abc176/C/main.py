#!/usr/bin/env python3

def main():
    input()
    cur = 0
    total = 0
    for a in [int(e) for e in input().split()]:
        if cur > a:
            total += cur - a
        else:
            cur = a
    print(total)


if __name__ == "__main__":
    main()
