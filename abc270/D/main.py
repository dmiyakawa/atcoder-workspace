#!/usr/bin/env python3
import bisect
from functools import lru_cache


def solve(N: int, K: int, A: "List[int]"):

    @lru_cache(10**8)
    def calc(n, t):
        ret_a = 0
        ret_b = 0
        for i in range(bisect.bisect_right(A, n)):
            a, b = calc(n - A[i], (t + 1) % 2)
            if t == 0:
                if ret_a < a + A[i]:
                    ret_a, ret_b = a + A[i], b
            else:
                if ret_b < b + A[i]:
                    ret_a, ret_b = a, b + A[i]
        return ret_a, ret_b

    ans_a, ans_b = calc(N, 0)
    print(ans_a)



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == "__main__":
    main()
