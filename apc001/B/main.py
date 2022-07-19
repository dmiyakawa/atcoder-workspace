#!/usr/bin/env python3


def solve(N: int, A: "List[int]", B: "List[int]"):
    num_holes = 0
    num_holes_2 = 0
    for a, b in zip(A, B):
        num_holes += max(0, a - b)
        num_holes_2 += max(0, (b - a) // 2)
    print("Yes" if num_holes_2 >= num_holes else "No")


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    solve(N, A, B)


if __name__ == "__main__":
    main()
