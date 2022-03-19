#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


def solve(N: int, A: "List[int]"):
    first_total = sum(A)
    final_total = N * (N - 1) // 2
    print(first_total)
    print(final_total)


if __name__ == "__main__":
    main()
