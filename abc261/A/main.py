#!/usr/bin/env python3

def main():
    L1, R1, L2, R2 = map(int, input().split())
    a = min(R1, R2) - max(L1, L2)
    print(a if a > 0 else 0)


if __name__ == "__main__":
    main()
