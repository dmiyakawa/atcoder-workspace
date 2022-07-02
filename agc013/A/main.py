#!/usr/bin/env python3

def main():
    int(input())
    A = [int(e) for e in input().split()]
    count = 0
    asc = None
    prev = None
    for a in A:
        if asc is not None:
            if asc and prev > a:
                count += 1
                asc = None
            elif not asc and prev < a:
                count += 1
                asc = None
        elif prev is not None:
            if prev < a:
                asc = True
            elif prev > a:
                asc = False
        prev = a
    count += 1
    print(count)


if __name__ == "__main__":
    main()
