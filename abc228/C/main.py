#!/usr/bin/env python3
from bisect import bisect

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N, K = [int(e) for e in input().split()]
    P = [sum(int(e) for e in input().split()) for _ in range(N)]
    Ps = sorted(P)
    for score in P:
        # 自分の低いスコア含めているので <= Kではなく < K
        print(YES if len(P) - bisect(Ps, score + 300) < K else NO)

if __name__ == "__main__":
    main()
