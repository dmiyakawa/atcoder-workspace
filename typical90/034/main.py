#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)


def solve(N: int, K: int, a: "List[int]"):
    d = {}
    max_length = 0
    si = 0
    for i in range(N):
        d[a[i]] = d.get(a[i], 0) + 1
        while len(d) > K:
            d[a[si]] -= 1
            if d[a[si]] == 0:
                del d[a[si]]
            si += 1
        max_length = max(max_length, i - si + 1)
    print(max_length)


if __name__ == "__main__":
    main()
