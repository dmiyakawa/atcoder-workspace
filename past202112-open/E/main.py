#!/usr/bin/env python3

def main():
    NS = input()
    total = 0
    prev_left = False
    prev_ch = None
    for i, ch in enumerate(NS):
        left = ch in {"1", "2", "3", "4", "5"}
        if i == 0:
            total += 500
        elif ch == prev_ch:
            total += 301
        elif left == prev_left:
            total += 210
        else:
            total += 100
        prev_left = left
        prev_ch = ch
    print(total)


if __name__ == "__main__":
    main()
