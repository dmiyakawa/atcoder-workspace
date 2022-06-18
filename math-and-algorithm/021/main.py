#!/usr/bin/env python3


def main():
    import math
    n, r = map(int, input().split())
    a = math.factorial(n)
    b = math.factorial(n - r)
    c = math.factorial(r)
    print(a // (b * c))


if __name__ == "__main__":
    main()
