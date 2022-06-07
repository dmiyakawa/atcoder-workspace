#!/usr/bin/env python3


def main():
    N = int(input())
    count = 0
    for n in range(1, N+1):
        if "7" not in str(n) + format(n, "o"):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
