#!/usr/bin/env python3
#
# - ベルトコンベア上の芋が尽きることはない
# - 箱詰めはあるk個目 (実装では loop_start_k, 0-origin) を境に同じパターンになる
# - 「同じパターン」の周期 (実装では loop_size) は芋の周期N以下なので検出をO(N)でできる
# - loop_start_k, loop_size の検出で O(N)、クエリは個別に O(1) で計 O(Q)。全体で O(N + Q)
#

import bisect


def main():
    N, Q, X = map(int, input().split())
    W = [int(e) for e in input().split()]
    W_sum = [0 for _ in range(N + 1)]
    W_sum2 = [0 for _ in range(N * 2 + 1)]
    for i in range(1, N + 1):
        W_sum[i] = W_sum[i - 1] + W[i - 1]
    for i in range(1, 2 * N + 1):
        W_sum2[i] = W_sum2[i - 1] + W[(i + N - 1) % N]

    W_total = W_sum[-1]
    X_loop = X // W_total
    X_m = X - X_loop * W_total

    num_i_d = {}
    num_potato_at_k_d = {}
    cur_k = 0
    cur_i = 0
    loop_start_k: int
    loop_size: int
    # print(f"W: {W}, W_sum: {W_sum}, W_sum2: {W_sum2}")
    # print(f"W_total: {W_total}, X_loop: {X_loop}")
    # print(f"N: {N}, X: {X}, X_m: {X_m}")
    while True:
        next_i = bisect.bisect_left(W_sum2, W_sum2[cur_i] + X_m)
        # 箱に詰め込む重さ
        box_weight = W_sum2[next_i] - W_sum2[cur_i]
        if box_weight < X_m:
            next_i += 1
            box_weight = W_sum2[next_i] - W_sum2[cur_i]
        # print(f"cur_i: {cur_i}, bisect_left({W_sum2}, {W_sum2[cur_i] + X_m})"
        # print(f" -> next_i: {next_i}, box_weight: {box_weight}")

        num_potato = next_i - cur_i + X_loop * N
        # print(f"cur_i: {cur_i}, next_i: {next_i}, box_weight: {box_weight}, num_potato: {num_potato}")

        num_i_d[cur_i] = (num_potato, cur_k)
        num_potato_at_k_d[cur_k] = num_potato
        # print(f"num_potato_at_k_d: {num_potato_at_k_d}")

        next_i %= N
        if next_i in num_i_d:
            _, loop_start_k = num_i_d[next_i]
            loop_size = cur_k + 1 - loop_start_k
            break
        cur_i = next_i
        cur_k += 1
    # print(f"loop_start_k: {loop_start_k}, loop_size: {loop_size}")

    for _ in range(Q):
        k = int(input()) - 1
        if loop_start_k > k:
            print(num_potato_at_k_d[k])
        else:
            print(num_potato_at_k_d[(k - loop_start_k) % loop_size + loop_start_k])



if __name__ == "__main__":
    main()
