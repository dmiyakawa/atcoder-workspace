#!/usr/bin/env python3
from collections import Counter


def main():
    input()
    c = Counter(int(e) for e in input().split())
    print(c.get(100, 0) * c.get(400, 0) + c.get(200, 0) * c.get(300, 0))


if __name__ == "__main__":
    main()
