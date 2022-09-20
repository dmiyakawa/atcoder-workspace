#!/usr/bin/env python3


def solve(X: int):
    lst = []
    for i, ch in enumerate(reversed(format(X, "b"))):
        if ch == "1":
            lst.append(i)

    for i in range(2 ** len(lst)):
        n = 0
        j = 0
        while i:
            if i & 1:
                n += 2**lst[j]
            i >>= 1
            j += 1
        print(n)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == "__main__":
    main()
