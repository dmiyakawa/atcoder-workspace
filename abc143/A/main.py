#!/usr/bin/env python3

def main():
    A, B = [int(e) for e in input().split()]
    if B * 2 >= A:
        print(0)
    else:
        print(A - B*2)


if __name__ == "__main__":
    main()
