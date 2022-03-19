#!/usr/bin/env python3

N = int(input())
A = [int(elem) for elem in input().split()]
B = [int(elem) for elem in input().split()]
C = [int(elem) for elem in input().split()]

# Ad, Bd, CdはそれぞれA, B, Cについての辞書で
# - key: それぞれの数字を46で余った余り。つまり0〜45
# - value: 0〜45の出る回数
Ad, Bd, Cd = {}, {}, {}

# N は最大で 10^5 。100,000。forループ一回なら大丈夫そうだ！
for i in range(N):
    a, b, c = A[i], B[i], C[i]
    Ad[a % 46] = Ad.get(a % 46, 0) + 1
    Bd[b % 46] = Bd.get(b % 46, 0) + 1
    Cd[c % 46] = Cd.get(c % 46, 0) + 1

# さぁ3重ループだ。でも酷く悲観的に見ても50*50*50=125000で、大した回数じゃない
count = 0
for a in range(0, 46):
    for b in range(0, 46):
        for c in range(0, 46):
            if (a + b + c) % 46 == 0:
                count += Ad.get(a, 0) * Bd.get(b, 0) * Cd.get(c, 0)

print(count, end="")
