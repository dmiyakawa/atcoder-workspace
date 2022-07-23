#!/usr/bin/env python3

from collections import Counter

def solve_ans(K, A):
    # 解説に基づく
    N = len(A)
    possible_max = sum(A) // K
    left, right = 0, possible_max
    while left < right:
        mid = (left + right + 1) // 2
        if sum(min(a, mid) for a in A) >= K * mid:
            left = mid
        else:
            right = mid - 1
    return left


def solve_wa_tle(K, A):
    # 遅いだけでなく論理的に間違い
    #
    # 構成的な方法で（具体的に作っていく場合に）正しくなるのは
    # 「Ai が大きい方からK個選んで「一つ」プロジェクトを作る場合」
    # であって
    # 「Ai が大きい方からK*X個選んで「X個」プロジェクトを作る場合」
    # ではない。後者だと、2個め以降を取るプロセスでAiが上位K個に含まれない部署を選び始めてしまい、不当に余る結果になる
    ans = 0
    while True:
        prev_ans = ans
        A = sorted(a for a in A if a > 0)
        if len(A) < K:
            break
        j = len(A) - K
        val = A[j]
        ans += val
        for l in range(K):
            A[j + l] -= val

        if prev_ans == ans:
            break

    return ans


def main():
    N, K = map(int, input().split())
    A = [int(e) for e in input().split()]
    print(solve_ans(K, A))


def _debug():
    from random import randint
    from timeit import timeit

    def _inter():
        N = randint(10**5, 2 * 10**5)
        K = randint(1, N)
        A = [randint(1, 10**12) if i < N // 2 else randint(10**11, 10**12) for i in range(N)]
        solve(K, A)

    print(max(timeit(_inter, number=1) for _ in range(10)))


if __name__ == "__main__":
    # _debug()
    main()
