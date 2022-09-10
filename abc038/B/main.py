#!/usr/bin/env python3

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(H: "List[int]", W: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = [int()] * (2)  # type: "List[int]"
    W = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        H[i] = int(next(tokens))
        W[i] = int(next(tokens))
    solve(H, W)


if __name__ == "__main__":
    main()
