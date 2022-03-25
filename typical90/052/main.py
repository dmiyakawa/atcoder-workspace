#!/usr/bin/env python3


MOD = 1000000007  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(6)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)


def solve(N: int, A: "List[List[int]]"):
    sums = [sum(A[0])]
    for i in range(1, N):
        sums.append(sum((sums[i - 1] * a) % MOD for a in A[i]) % MOD)
    print(sums[-1], end="")


if __name__ == "__main__":
    main()
