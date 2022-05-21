#!/usr/bin/env python3

def main():
    a = int(input())
    b = int(input())
    print((b - a % b) % b)


if __name__ == "__main__":
    main()
