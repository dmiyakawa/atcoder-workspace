#!/usr/bin/env python3


def solve(N: int, K: int, A: "List[int]"):
    max_A = max(A)
    l, r = 1, max_A
    mid = r
    while l < r:
        mid = (l + r) // 2 + (l + r) % 2
        if mid == r:
            mid -= 1
        rem = K
        successful = True
        for a in A:
            rem -= a // mid + (1 if a % mid else 0) - 1
            if rem < 0:
                successful = False
                break
        if successful:
            r = mid
        else:
            l = mid + 1
    assert l == r
    print(r)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == "__main__":
    main()
