#!/usr/bin/env python3


def main():
    N = int(input())
    submitted = set()
    lst = []
    for i in range(1, N + 1):
        S, b = input().split()
        T = int(b)
        if S in submitted:
            T = -1
        else:
            submitted.add(S)
        lst.append((S, T, i))
    lst.sort(key=lambda key: (-key[1], key[2]))
    print(lst[0][2])


if __name__ == "__main__":
    main()
