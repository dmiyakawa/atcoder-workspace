#!/usr/bin/env python3

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    t, b, l, r = 1, N, 1, N
    while b - t > 0 or r - l > 0:
        if b - t > 0:
            m = (b + t) // 2
            print(f"? {t} {m} {1} {N}", flush=True)
            n = int(input())
            if n < 0:
                return
            if n < m - t + 1:
                b = m
            else:
                t = m + 1
            continue
        if r - l > 0:
            m = (l + r) // 2
            print(f"? {1} {N} {l} {m}", flush=True)
            n = int(input())
            if n < 0:
                return
            if n < m - l + 1:
                r = m
            else:
                l = m + 1
    print(f"! {t} {l}", flush=True)


if __name__ == "__main__":
    main()
