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
    # 解説確認済み
    if A[-1] - A[-2] > 1:
        winner = "Alice"
    elif (A[-1] - (N - 1)) % 2 == 1:
        winner = "Alice"
    else:
        winner = "Bob"
    print(winner, end="")


if __name__ == "__main__":
    main()
