#!/usr/bin/env python3


def solve(N: int, p: "List[int]"):
    counts = [0] * N
    for i in range(N):
        counts[(p[i] - i - 1) % N] += 1
        counts[(p[i] - i) % N] += 1
        counts[(p[i] - i + 1) % N] += 1
        # print(counts)
    print(max(counts))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)


if __name__ == "__main__":
    main()
