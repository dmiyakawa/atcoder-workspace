#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    lst = []
    total = 0
    for a in A:
        if lst and lst[-1][0] == a:
            (_, n) = lst.pop()
            if n + 1 == a:
                total -= n
            else:
                lst.append((a, n + 1))
                total += 1
        else:
            lst.append((a, 1))
            total += 1
        print(total)


if __name__ == "__main__":
    main()
