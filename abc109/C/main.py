#!/usr/bin/env python3

def main():
    from functools import reduce
    from math import gcd
    N, X = [int(e) for e in input().split()]
    print(reduce(lambda x, y: gcd(x, y), (abs(int(e) - X) for e in input().split())))


if __name__ == "__main__":
    main()
