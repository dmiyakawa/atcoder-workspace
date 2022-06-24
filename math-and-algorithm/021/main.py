#!/usr/bin/env python3

import math

n, r = map(int, input().split())

print(math.factorial(n) // (math.factorial(n - r) * math.factorial(r)))
