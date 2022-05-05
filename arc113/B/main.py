#!/usr/bin/env python3


def main():
    A, B, C = [int(e) for e in input().split()]
    print(calc(A, B, C))


def calc(A, B, C):
    # >>> from pprint import pprint
    # >>> pprint([[i**n % 10 for n in range(1, 11)] for i in range(10)])
    # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #  [2, 4, 8, 6, 2, 4, 8, 6, 2, 4],
    #  [3, 9, 7, 1, 3, 9, 7, 1, 3, 9],
    #  [4, 6, 4, 6, 4, 6, 4, 6, 4, 6],
    #  [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
    #  [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
    #  [7, 9, 3, 1, 7, 9, 3, 1, 7, 9],
    #  [8, 4, 2, 6, 8, 4, 2, 6, 8, 4],
    #  [9, 1, 9, 1, 9, 1, 9, 1, 9, 1]]
    a_mod = A % 10
    if a_mod in [0, 1, 5, 6]:
        return a_mod
    elif a_mod in [4, 9]:
        return a_mod ** 2 % 10 if B % 2 == 0 else a_mod % 10
    # 2, 3, 7, 8は周期4
    if B % 4 == 0:
        # B = 4n
        # Cに関係なく常に4の倍数で周期4にぴったり合う
        return a_mod ** 4 % 10
    if B % 4 == 1:
        # B = 4n + 1
        return a_mod % 10
    if B % 4 == 2:
        # B = 4n + 2
        if C == 1:
            return a_mod ** 2 % 10
        else:
            return a_mod ** 4 % 10
    # B = 4n + 3
    if C % 2 == 0:
        return a_mod % 10
    else:
        return a_mod ** 3 % 10


def check():
    for A in range(4, 10):
        for B in range(1, 10):
            for C in range(1, 10):
                ans = A ** (B ** C) % 10
                if calc(A, B, C) != ans:
                    print(f"{A} {B} {C} -> {calc(A, B, C)} != ans: {ans}")
                    return
    print("All correct for this range")


if __name__ == "__main__":
    main()
