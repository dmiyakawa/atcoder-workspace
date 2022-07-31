#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(B: int, C: int):
    ans = 1  # 0円使った際にBを得られる
    if B > 0:
        # [0, B-1] は 2 円ずつ払うことで到達
        a = min(B, C // 2)
        # [-B, -1] は必要な回数分 2 円払ってかつ1円で反転。B個分よりは増えない
        b = min(B, max(C + 1, 0) // 2)
        # -B より小さい数値 D には 1 円払って反転後に2をその回数分
        c = max(C - 1, 0) // 2
        # B より大きい数値 E には D の操作に加えて 1 円払って反転
        d = max(C - 2, 0) // 2
        # print(a, b, c, d)
        ans += a + b + c + d
    else:
        # B より小さい数値 D (< 0) には 2円 を (B - D) 回数分
        a = C // 2
        # -B より大きい数値 -D (> -B) には 1円払って反転して回数分
        b = (C - 1) // 2
        # (0, -B] は 1円払って反転して2円を回数分行う
        c = min(abs(B), max(C + 1, 0) // 2)
        # [B + 1, 0] は 1円払って反転して2円を回数分行い1円払って再度反転
        d = min(abs(B), max(C - 2, 0) // 2)
        ans += a + b + c + d

    print(ans)



def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(B, C)


if __name__ == "__main__":
    main()
