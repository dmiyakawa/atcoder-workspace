#!/usr/bin/env python3


def solve(N: int, S: "List[str]"):
    count = 1
    ans = 1
    for i, s in enumerate(S[::-1]):
        if s == "OR":
            ans += 2 ** (N - i)
    print(ans)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == "__main__":
    main()
