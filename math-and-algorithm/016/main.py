#!/usr/bin/env python3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while True:
        m = a % b
        if m == 0:
            break
        else:
            a, b = b, a % b
    return b


def main():
    input()
    A = [int(e) for e in input().split()]
    val = A[0]
    for a in A[1:]:
        val = gcd(val, a)
    print(val)


if __name__ == "__main__":
    main()
