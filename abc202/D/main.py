#!/usr/bin/env python3

import math

def main():
    A, B, K = map(int, input().split())
    k = K - 1
    lst = []
    while A > 0 or B > 0:
        if A == 0:
            lst.extend(["b"] * B)
            break
        elif B == 0:
            lst.extend(["a"] * A)
            break
        v = math.factorial(A + B - 1) // (math.factorial(A - 1) * math.factorial(B))
        if k < v:
            lst.append("a")
            A -= 1
        else:
            k -= v
            lst.append("b")
            B -= 1
    print("".join(lst))


if __name__ == "__main__":
    main()
