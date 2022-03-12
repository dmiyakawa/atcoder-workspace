#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    t = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(Q, t, x)


def solve(Q: int, t: "List[int]", x: "List[int]"):
    return


if __name__ == "__main__":
    main()
