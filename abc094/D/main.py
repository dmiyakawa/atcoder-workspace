#!/usr/bin/env python3

import bisect

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    A.sort()
    a = A[N - 1]
    i = bisect.bisect(A, a / 2)
    cands = []
    if i > 0:
        cands.append(A[i - 1])
    if i > 1:
        cands.append(A[i - 2])
    if i < N - 1:
        cands.append(A[i])
    if i < N - 2:
        cands.append(A[i + 1])

    b = sorted(cands, key=lambda cand: abs(A[N - 1] / 2 - cand))[0]
    print(a, b)



if __name__ == "__main__":
    main()
