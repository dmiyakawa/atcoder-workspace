#!/usr/bin/env python3

def main():
    import math
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int

    max_cand = -1
    for r in range(R, L, -1):
        if r - L < max_cand:
            break
        for l in range(L, r):
            cand = r - l
            if r - l < max_cand:
                break
            elif math.gcd(l, r) == 1:
                if max_cand == -1 or cand > max_cand:
                    max_cand = cand
                break
    print(max_cand, end="")


if __name__ == "__main__":
    main()
