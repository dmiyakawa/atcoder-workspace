#!/usr/bin/env python3



def solve(N: int, S: str):
    dp1 = [False] * 10
    dp2 = [False] * 100
    dp3 = [False] * 1000
    for s in S:
        v = int(s)
        for i in range(100):
            if dp2[i]:
                dp3[i * 10 + v] = True
        for i in range(10):
            if dp1[i]:
                dp2[i * 10 + v] = True
        dp1[v] = True
    print(dp3.count(True))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == "__main__":
    main()
