#!/usr/bin/env python3

def main():
    total = 0
    for i in range(3):
        s, e = [int(e) for e in input().split()]
        total += s * e // 10
    print(total)


if __name__ == "__main__":
    main()
