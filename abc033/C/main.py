#!/usr/bin/env python3


def solve(S: str):
    ans = 0
    for s in S.split("+"):
        if "0" not in s:
            ans += 1
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
