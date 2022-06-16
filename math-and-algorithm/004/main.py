#!/usr/bin/env python3
from functools import reduce

print(reduce(lambda x, y: x * y, (int(e) for e in input().split())))
