#!/usr/bin/env python3


def main():
    N = int(input())
    print(sum(int(e) / N for e in input().split()) + sum(int(e) / N for e in input().split()))


if __name__ == "__main__":
    main()
