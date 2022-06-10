#!/usr/bin/env python3


def solve_by_doubling(N, K, A):
    # 以下の解法2
    # https://atcoder.jp/contests/abc241/editorial/3472
    import math
    dp = [A]
    for k in range(1, int(math.log2(K)) + 1):
        lst = []
        dp.append(lst)
        for j in range(N):
            dp[k].append(dp[k - 1][j] + dp[k - 1][(j + dp[k - 1][j]) % N])
    total = 0
    i = 0
    while K:
        if K % 2:
            total += dp[i][total % N]
        i += 1
        K //= 2
    print(total)


def solve_by_cycle_detection(N, K, A):
    # K <= 10 ^ 12 と非常に大きいのでK回の操作を愚直に行うのは無理
    # N <= 2 * 10^5 であるため、K回操作をするはるか手前で以前と同じ A_i を参照する（巡回グラフとなる）のは間違いない
    # ぐるぐる回る輪っかを見つけてその輪っかのサイズでKの残りを割り「何周回ったか」と「残りで輪っかのどこまでいくか」を計算すればそこはO(1)
    # トータルで O(N) 解法
    first_contact = [-1 for _ in range(N)]
    prev_count = -1
    count = 0
    count_as_of = []
    i = 0
    # N回以内に巡回を検出して止まる
    while first_contact[count % N] < 0 and 0 < K:
        count_as_of.append(count)
        first_contact[count % N] = i
        prev_count = count
        count += A[count % N]
        K -= 1
        i += 1
    # Kの残りは輪のなかをぐるぐる
    cycle_length = first_contact[prev_count % N] - first_contact[count % N] + 1
    cycle_count = count_as_of[first_contact[prev_count % N]] - count_as_of[first_contact[count % N]] + A[prev_count % N]
    print(count + (K // cycle_length) * cycle_count
          + count_as_of[first_contact[count % N] + (K % cycle_length)] - count_as_of[first_contact[count % N]])


def main():
    N, K = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    solve_by_doubling(N, K, A)
    # solve_by_cycle_detection(N, K, A)


if __name__ == "__main__":
    main()
