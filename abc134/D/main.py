#!/usr/bin/env python3


def solve(N: int, a: "List[int]"):
    b = [-1] * N
    ans = []

    for n in range(N, 0, -1):
        i = n - 1
        c = 0
        for m in range(2, N + 1):
            if n * m > N:
                break
            c += b[n * m - 1]
        c %= 2
        b[i] = c ^ a[i]
        # print(n, i, c, a[i], b[i])
        if b[i]:
            ans.append(n)

    print(len(ans))
    if ans:
        print(*ans)



def make_divisors(n):
    """nの約数を列挙する"""
    # https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def main():
    N = int(input())
    a = list(map(int, input().split()))
    # デバッグ用
    if N == 0:
        N = len(a)
    solve(N, a)


def _debug():
    from random import randint
    N = 10**5
    # a = [randint(0, 1) for _ in range(N)]
    a = [0] * N
    print(N)
    print(*a)
    # solve(N, a)


if __name__ == "__main__":
    # _debug()
    main()
