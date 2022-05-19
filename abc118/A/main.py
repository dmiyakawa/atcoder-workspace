#!/usr/bin/env python3

def main():
    A, B = [int(e) for e in input().split()]
    print(A + B if B % A == 0 else B - A)


if __name__ == "__main__":
    main()
