#!/usr/bin/env python3

Inf = float("inf")


def solve(N: int, A: "List[int]", T: "List[int]", Q: int, X: "List[int]"):
    l, m, r = -Inf, 0, Inf
    for t, a in zip(T, A):
        if t == 1:
            m += a
        elif t == 2:
            l = max(l, a + m)
        else:
            r = min(r, a - m)
    print("#", l, m, r)
    for x in X:
        print(min(max(x, l), r) + m)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        t[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, a, t, Q, x)


if __name__ == "__main__":
    main()
