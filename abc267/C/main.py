#!/usr/bin/env python3



def solve(N: int, M: int, A: "List[int]"):
    B = A.copy()
    for i in range(1, N):
        B[i] += B[i - 1]
    cur = sum((i + 1) * A[i] for i in range(M))
    ans = cur
    for i in range(M, N):
        cur = cur + M * A[i] - (B[i - 1] - (B[i - 1 - M] if i - 1 - M >= 0 else 0))
        ans = max(ans, cur)
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
