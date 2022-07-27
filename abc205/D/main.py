#!/usr/bin/env python3
import bisect
import sys

def solve(N: int, Q: int, A: "List[int]", K: "List[int]"):
    for k in K:
        prev_rem = 0
        while True:
            rem = bisect.bisect_right(A, k + prev_rem)
            if rem == prev_rem:
                print(k + rem)
                break
            prev_rem = rem


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    K = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, K)





if __name__ == "__main__":
    main()
