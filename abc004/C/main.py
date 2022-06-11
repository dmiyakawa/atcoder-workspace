#!/usr/bin/env python3

s = {}

def main():
    N = int(input())
    c = (1, 2, 3, 4, 5, 6)
    d = {}
    for i in range(N):
        values = list(c)
        left = n % 5
        right = (n + 1) % 5
        values[left], values[right] = values[right], values[left]
        next_c = tuple(values)
        key = (n % 5, next_c)

        if key in d:
            print(d[key], n)
            break
        d[key] = n
        c = next_c
    print(d)


if __name__ == "__main__":
    main()
