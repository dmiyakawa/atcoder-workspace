#!/usr/bin/env python3


def main():
    N, A, B = [int(e) for e in input().split()]
    print(min(N, 5) * B + (N - min(N, 5)) * A)


if __name__ == "__main__":
    main()
