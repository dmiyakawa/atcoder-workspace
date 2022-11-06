#!/usr/bin/env python3

MOD = 3  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, Q: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]", e: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    d = [int()] * (Q)  # type: "List[int]"
    e = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
        e[i] = int(next(tokens))
    solve(N, Q, a, b, c, d, e)


if __name__ == "__main__":
    main()
