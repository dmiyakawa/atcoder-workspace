#!/usr/bin/env python3

K, X = map(int, input().split())

lst = [i for i in range(X - K + 1, X + K)]
print(*lst)
