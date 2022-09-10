#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, W: int, S: "List[int]", T: "List[int]", P: "List[int]"):
    lst = [0] * (2*10**5 + 1)
    for s, t, p in zip(S, T, P):
        lst[s] += p
        lst[t] -= p
    total = 0
    for v in lst:
        total += v
        if total > W:
            print(NO)
            return
    print(YES)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, W, S, T, P)


if __name__ == "__main__":
    main()
