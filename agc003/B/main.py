#!/usr/bin/env python3



def solve(N: int, A: "List[int]"):
    ans = 0
    for i in range(N):
        ans += A[i] // 2
        A[i] %= 2
        if A[i] > 0 and i < N - 1 and A[i + 1] > 0:
            ans += 1
            A[i] = 0
            A[i + 1] -= 1
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
