#!/usr/bin/env python3
from collections import Counter


def main():
    N, K = map(int, input().split())
    counter = Counter(int(e) for e in input().split())
    lst = sorted(counter.items(), key=lambda tup: tup[1])
    print(sum(value for _, value in lst[:-K]))


if __name__ == "__main__":
    main()
