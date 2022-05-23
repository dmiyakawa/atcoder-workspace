#!/usr/bin/env python3

count = 0
cur_ch = None
lst = []
for ch in input():
    if cur_ch != ch:
        if cur_ch is not None and count > 0:
            lst.append("{}{}".format(cur_ch, count))
        cur_ch = ch
        count = 1
    else:
        count += 1
if count > 0:
    lst.append("{}{}".format(cur_ch, count))

print("".join(lst))
