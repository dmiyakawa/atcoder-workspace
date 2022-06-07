#!/usr/bin/env python3


def main():
    N = int(input())
    lst = []
    while N > 0:
        if N % 2 == 1:
            N -= 1
            lst.append("A")
        if N > 0:
            N //= 2
            lst.append("B")
    lst.reverse()
    print("".join(lst))


if __name__ == "__main__":
    main()
