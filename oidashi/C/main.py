#!/usr/bin/env python3



def solve(n: int, s: "List[int]", c: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    s = [int()] * (n)  # type: "List[int]"
    c = [int()] * (n)  # type: "List[int]"
    for i in range(n):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(n, s, c)


if __name__ == "__main__":
    main()
