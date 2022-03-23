#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    x = [int()] * (2)  # type: "List[int]"
    y = [int()] * (2)  # type: "List[int]"
    r = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(x, y, r)


def solve(x: "List[int]", y: "List[int]", r: "List[int]"):
    return


if __name__ == "__main__":
    main()
