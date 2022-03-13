#!/usr/bin/env python3

import random

import ans_1
import main


if __name__ == "__main__":
    i = 0
    while True:
        if i % 100 == 0:
            print(i)
        T = 20
        L = [random.randrange(1, 10 ** 19) for _ in range(T)]
        a = ans_1.calc(T, L)
        try:
            b = main.calc(T, L)
            if a != b:
                print(f"theirs: {a} != ours: {b}")
                break
        except Exception as e:
            print(f"ours caused an Exception {e} with {L} ({type(e)}")
            break
        i += 1

