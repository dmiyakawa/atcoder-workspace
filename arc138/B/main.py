#!/usr/bin/env python3

import sys
from typing import List

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(YES if solve(N, A) else NO)


def solve(N: int, A: "List[int]"):
    left = 0
    right = N - 1
    flipped = False
    while left <= right:
        one = 1 if not flipped else 0
        while A[right] != one:
            right -= 1
            if right < left:
                break
        if right < left:
            continue
        if A[left] == one and A[right] == one:
            return False
        if A[left] != one:
            left += 1
            flipped = not flipped
    return True


if __name__ == "__main__":
    main()
