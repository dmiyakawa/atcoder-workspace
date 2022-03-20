#!/usr/bin/env python3


def main():
    import math
    import sys
    A, B = [int(e) for e in sys.stdin.readline().split()]
    muls = 1
    a, b = A, B
    while True:
        gcd = math.gcd(a, b)
        if gcd == 1:
            break
        muls *= gcd
        a = A // muls
        b = B // muls
    lcd = a * b * muls
    ans = "Large" if lcd > 10 ** 18 else lcd
    print(ans, end="")


if __name__ == "__main__":
    main()
