#!/usr/bin/env python3

MOD = 1000000007  # type: int


def main():
    _ = int(input())
    A = [int(e) for e in input().split()]
    A.sort()
    combination = 1
    if len(A) % 2 == 1:
        # 0 2 2 4 4 6 6 8 8 ...
        for i, a in enumerate(A):
            if ((i + 1) // 2) * 2 != a:
                combination = 0
                break
            if (i + 1) % 2 == 0:
                combination = (combination * 2) % MOD
    else:
        # 1 1 3 3 5 5 7 7 9 9 ...
        for i, a in enumerate(A):
            if (i // 2) * 2 + 1 != a:
                combination = 0
                break
            if i % 2 == 0:
                combination = (combination * 2) % MOD

    print(combination)


if __name__ == "__main__":
    main()
