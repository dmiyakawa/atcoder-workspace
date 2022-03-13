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
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)


def solve(N: int, A: "List[int]", B: "List[int]"):
    print(sum(abs(a - b) for a, b in zip(sorted(A), sorted(B))), end="")


if __name__ == "__main__":
    main()
