#!/usr/bin/env python3

def main():
    A, B = [int(e) for e in input().split()]
    if A < 10 and B < 10:
        print(A * B)
    else:
        print(-1)


if __name__ == "__main__":
    main()
