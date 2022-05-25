#!/usr/bin/env python3
m = int(input())

if m < 100:
    print("00")
elif m <= 5000:
    print("{:02d}".format(m//100))
elif m <= 30000:
    print("{:02d}".format(m//1000 + 50))
elif m <= 70000:
    print("{:02d}".format((m//1000 - 30) // 5 + 80))
else:
    print(89)

