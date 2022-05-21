#!/usr/bin/env python3

def main():
    a = int(input())
    b = int(input())
    if abs(a - b) > 5:
        print(10 - abs(a - b))
    else:
        print(abs(a - b))


if __name__ == "__main__":
    main()
