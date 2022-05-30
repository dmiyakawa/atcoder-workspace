#!/usr/bin/env python3
input()
s = {int(e) for e in input().split()}
input()
yes = True
for p in [int(e) for e in input().split()]:
    if p in s:
        yes = False
        break
    else:
        s.add(p)
print("YES" if yes else "NO")
