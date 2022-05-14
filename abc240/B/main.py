#!/usr/bin/env python3

def main():
    N = int(input())
    a = [int(e) for e in input().split()]
    solve(N, a)


def solve(N: int, a: "List[int]"):
    s = set(a)
    print(len(s))


if __name__ == "__main__":
    main()
