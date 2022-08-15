#!/usr/bin/env python3

def solve(N: int, A: "List[int]"):
    max_takahashi = -10**9
    for i in range(N):
        max_aoki = -10**9
        max_j = -1
        for j in range(N):
            if i == j:
                continue
            takahashi = 0
            aoki = 0
            left = min(i, j)
            right = max(i, j)
            for k in range(right - left + 1):
                if k % 2 == 0:
                    takahashi += A[left + k]
                else:
                    aoki += A[left + k]

            if aoki > max_aoki:
                max_aoki = aoki
                max_j = j
                # print(i, j, A[i:right + 1], takahashi, max_aoki)
        left = min(i, max_j)
        right = max(i, max_j)
        max_takahashi = max(max_takahashi, sum(A[left + k] for k in range(right - left + 1) if k % 2 == 0))
    print(max_takahashi)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
