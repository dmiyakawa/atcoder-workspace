#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, Q, A, T, x, y)


def solve(N: int, Q: int, A: "List[int]", T: "List[int]", x: "List[int]", y: "List[int]"):
    offset = 0
    for i in range(Q):
        ti, xi, yi = T[i], x[i] - 1, y[i] - 1
        if ti == 1:
            xio = (xi + offset) % N
            yio = (yi + offset) % N
            A[xio], A[yio] = A[yio], A[xio]
        elif ti == 2:
            offset = (offset + N - 1) % N
        elif ti == 3:
            print(A[(xi + offset) % N])


if __name__ == "__main__":
    main()
