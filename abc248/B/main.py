#!/usr/bin/env python3

def main():
    A, B, K = [int(e) for e in input().split()]
    count = 0
    while A < B:
        A *= K
        count +=1
    print(count)


if __name__ == "__main__":
    main()
