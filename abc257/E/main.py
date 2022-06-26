#!/usr/bin/env python3


def solve(N, C):
    ...



def solve_wa(N: int, C):
    # 桁数最大化に近いところまで行ったが実装はダメ
    max_cont = 0
    max_cont_i = 0
    for i in range(len(C) - 1, -1, -1):
        c = C[i]
        if max_cont < max(N // c - 5, 0):
            max_cont = max(N // c - 5, 0)
            max_cont_i = i
    part1 = max_cont * str(max_cont_i + 1)
    N -= max_cont * C[max_cont_i]
    part2 = str(solve_tle(N, C))
    return max(int(part1 + part2), int(part2 + part1))


def solve_tle(N: int, C):
    dp = [0 for _ in range(N + 1)]
    cur_max = -1
    for n in range(N, -1, -1):
        cur = dp[n]
        if cur > cur_max:
            cur_max = cur
        else:
            continue
        for i, c in enumerate(C, start=1):
            if n - c >= 0 and cur * 10 + i > dp[n - c]:
                dp[n - c] = cur * 10 + i
    return max(dp)


def main():
    N = int(input())
    C = [int(e) for e in input().split()]
    print(solve(N, C))
    # solve_tle(N, C)


if __name__ == "__main__":
    main()
