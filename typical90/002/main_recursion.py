#!/usr/bin/env python3


def f(current_str, num_remaining, num_pending):
    if num_remaining == 0 and num_pending == 0:
        print(current_str)
    else:
        if num_remaining > 0:
            f(current_str + "(", num_remaining - 1, num_pending + 1)
        if num_pending > 0:
            f(current_str + ")", num_remaining, num_pending - 1)


N = int(input())
if N % 2 == 0:
    f("", N // 2, 0)
