#!/usr/bin/env python3
import bisect

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, P: int, Q: int, R: int, A: "List[int]"):
    B = [a for a in A]
    for i in range(1, N):
        B[i] += B[i - 1]
    # print(B)
    PQR = P + Q + R
    r = 0
    # print(PQR)
    for l in range(N):
        while r < N:
            lv = B[l - 1] if l > 0 else 0
            total = B[r] - lv
            # print(l, r, total)
            if total > PQR:
                break
            elif total == PQR:
                pi = bisect.bisect_left(B, P + lv, lo=l, hi=r + 1)
                qi = bisect.bisect_left(B, P + Q + lv, lo=l, hi=r + 1)
                # print(pi, B[pi] - lv, qi, B[qi] - B[pi])
                if B[pi] - lv == P and B[qi] - B[pi] == Q:
                    return True
            r += 1

    return False


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(YES if solve(N, P, Q, R, A) else NO)


if __name__ == "__main__":
    main()
