#!/usr/bin/env python3

def main():
    import math

    N = int(input())

    for n in range(2, int(math.sqrt(N)) + 1):
        if N % n == 0:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()


