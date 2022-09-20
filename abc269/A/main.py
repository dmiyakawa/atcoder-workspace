#!/usr/bin/env python3



def solve(a: int, b: int, c: int, d: int):
    print((a + b) * (c - d))
    print("Takahashi")
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(a, b, c, d)


if __name__ == "__main__":
    main()
