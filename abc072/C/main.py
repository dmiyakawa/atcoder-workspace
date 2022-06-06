#!/usr/bin/env python3

def main():
    int(input())
    d = {}
    for a in [int(e) for e in input().split()]:
        d[a - 1] = d.get(a - 1, 0) + 1
        d[a] = d.get(a, 0) + 1
        d[a + 1] = d.get(a + 1, 0) + 1

    print(max(d.values()))


if __name__ == "__main__":
    main()
