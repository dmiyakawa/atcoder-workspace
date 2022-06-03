#!/usr/bin/env python3


MOD = 1000000007  # type: int


def solve(N: int, S: str):
    d = {}
    for ch in S:
        d[ch] = d.get(ch, 0) + 1
    count = 1
    for value in d.values():
        count = count * (value + 1) % MOD

    print(count - 1)


def main():
    N = int(input())
    S = input()
    solve(N, S)


if __name__ == "__main__":
    main()
