#!/usr/bin/env python3

def main():
    N = int(input())
    N = N % 30
    lst = [1, 2, 3, 4, 5, 6]
    for i in range(N):
        lst[i % 5], lst[i % 5 + 1] = lst[i % 5 + 1], lst[i % 5]
    print("".join(str(val) for val in lst))


if __name__ == "__main__":
    main()
