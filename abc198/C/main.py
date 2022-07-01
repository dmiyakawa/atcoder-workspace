#!/usr/bin/env python3

import math

def main():
    R, X, Y = [int(e) for e in input().split()]
    d = math.sqrt(X*X + Y*Y)
    if d < R:
        print(2)
    else:
        print(math.ceil(d / R))


if __name__ == "__main__":
    main()
