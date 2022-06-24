#!/usr/bin/env python3


def solve(N: int, K: int, S: int):
    lst = [S] * K
    rem = N - K
    if S == 10**5:
        lst.extend([10**5 - 1] * rem)
    elif S < 10**5:
        lst.extend([10**5] * rem)
    else:
        lst.extend([1] * rem)
    return lst


def main():
    N, K, S = map(int, input().split())
    print(*solve(N, K, S))


if __name__ == "__main__":
    main()
