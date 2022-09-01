#!/usr/bin/env python3


def solve(N: int, X: "List[int]", Y: "List[int]"):
    points = sorted((x, y) for x, y in zip(X, Y))
    points_set = set(points)
    count = 0
    for i in range(N):
        x0, y0 = X[i], Y[i]
        for j in range(N):
            x1, y1 = X[j], Y[j]
            if not (x0 < x1 and y0 < y1):
                continue
            if (x0, y1) in points_set and (x1, y0) in points_set:
                # print((x0, y0), (x0, y1), (x1, y0), (x1, y1))
                count += 1
    print(count)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)


if __name__ == "__main__":
    main()
