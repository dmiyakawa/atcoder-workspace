#!/usr/bin/env python3
S = input()
T = input()
s = []
t = []
for ch in S:
    if ch == "@":
        s.append(set("atcoder"))
    else:
        s.append({ch})
for ch in T:
    if ch == "@":
        t.append(set("atcoder"))
    else:
        t.append({ch})

win = True
for s1, t1 in zip(s, t):
    if not (s1 & t1):
        win = False
        break

print("You can win" if win else "You will lose")

