#!/usr/bin/env python3

def main():
    N = int(input())
    lst = [tuple(int(e) for e in input().split()) for _ in range(N)]
    lst.sort(key=lambda tup: tup[1])
    count = 0
    r0 = None
    for l, r, in lst:
        if r0 is not None and l <= r0:
            continue
        count += 1
        r0 = r
    print(count)


if __name__ == "__main__":
    main()
