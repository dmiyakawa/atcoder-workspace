#!/usr/bin/env python3


def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        org_t, org_k = [int(e) for e in input().split()]
        t = org_t
        k = org_k - 1
        seq = []
        # k < 10**18 < 2**60 で、t > 60 のときにはkは0に潰れる
        # ループは最大60回
        while t > 0 and k > 0:
            seq.append(k % 2 + 1)
            k //= 2
            t -= 1
        # まだ t ~= 10**18 といった状況もあり得るが % 3 で定数コストの計算
        # A = 0, B = 1, C = 2 としたとき、S[0], S[0] + 1, S[0] + 2で繰り返す
        n = (ord(S[k]) - ord("A") + t) % 3

        # print(f"t: {org_t} -> {t}, k: {org_k} -> {k}, n: {n}, seq: {seq}")

        # seqは木を逆方向にたどっていって根となる"A"〜"C"までの分岐を記録したもの
        # 根(A -> 0, B -> 1, C -> 2)から分岐の左(+1)右(+2)を足す(mod 3)
        for a in reversed(seq):
            n += a

        print(chr(n % 3 + ord("A")))


if __name__ == "__main__":
    main()
