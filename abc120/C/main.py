#!/usr/bin/env python3

from collections import Counter
c = Counter(input())
if len(c) == 1:
    print(0)
else:
    print(min(c.values()) * 2)
