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
    c = [next(tokens) for _ in range(N)]  # type: "List[str]"
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, c, a, b)


def solve(N: int, c: "List[str]", a: "List[int]", b: "List[int]"):
    return


if __name__ == "__main__":
    main()
