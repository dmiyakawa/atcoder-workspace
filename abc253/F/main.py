#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def my_bisect(lst, i, left=None, right=None) -> int:
    if left is None:
        left = 0
    if right is None:
        right = len(lst)
    mid_index = (left + right) // 2
    mid = lst[mid_index]

    if mid[0] <= i <= mid[1]:
        return mid_index
    elif i < mid[0]:
        return my_bisect(lst, i, left=left, right=mid_index)


def main():
    N, M, Q = [int(e) for e in input().split()]
    row_values = [0, N, 0]
    col_offsets = [[0, M, 0]]
    for i in range(Q):
        query = [int(e) for e in input().split()]
        op = query[0]
        if op == 1:
            l, r, x = query[1] - 1, query[2] - 1, query[3]
            l_index: int = my_bisect(col_offsets, l)
            r_index: int = my_bisect(col_offsets, r)
            assert l_index <= r_index  # RE落とし
            if l_index == r_index:
                # < ( ) > -> (L) <M> (R)
                col = col_offsets[l_index]

                if r + 1 < col[1]:
                    # R を新規に挿入
                    col_offsets.insert(l_index + 1, [r + 1, col[1], col[2]])

                if col[0] < l:
                    # L を新規に挿入
                    col_offsets.insert(l_index, [col[0], l, col[2]])
                # 既存の col を M に適合する形で修正
                col[0] = l
                col[1] = r + 1
                col[2] = col[2] + x
            else:
                col_l = col_offsets[l_index]
                col_r = col_offsets[r_index]
                # < ( > [ ] [ ] ... [ ] < ) > の [ ] に対する取り扱い
                if r_index - l_index > 0:
                    for mid_index in range(l_index + 1, r_index):
                        col_offsets[mid_index][2] += x
                # < ( > < ) > -> <L> (M) <R>
                if r + 1 < col_r[1]:
                    col_r[0] = r + 1
                else:
                    # R が要らないので削除する
                    del col_offsets[r_index]

                if col_l[0] < l:
                    # L を新たに挿入する
                    col_offsets.insert(l_index, [col_l[0], l, col_l[2]])

                # 既存の col_l を再利用して M とする
                col_l[0] = l
                col_l[1] = r + 1
                col_l[2] += x

        elif op == 2:
            i, x = query[1] - 1, query[2]
        else:
            i, j = query[1] - 1, query[2] - 1
            offset_index = my_bisect(col_offsets, j)
            offset = col_offsets[offset_index][2]
            col_index = my_bisect(cols, j)
            col = cols[col_index]
            print(col[2] + offset)


if __name__ == "__main__":
    main()
