#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    print(solve(N, X, Y))


def solve(N: int, X: "List[int]", Y: "List[int]"):
    import math
    if sum(X) % len(X) == 0 and sum(Y) % len(Y) == 0:
        # print(sum(X) // len(X), sum(Y) // len(Y))
        return manhattan_total(sum(X) // len(X), sum(Y) // len(Y), X, Y)
    mean_x, mean_y = sum(X)/len(X), sum(Y)/len(Y)
    min_total = 10**18
    for x1, y1 in {(math.floor(mean_x), math.floor(mean_y)),
                   (math.ceil(mean_x), math.floor(mean_y)),
                   (math.ceil(mean_x), math.ceil(mean_y)),
                   (math.floor(mean_x), math.ceil(mean_y))}:
        for i in range(-5, 6):
            for j in range(-5, 6):
                x, y = x1 + i, y1 + j
                # print(x, y, manhattan_total(x, y, X, Y))
                min_total = min(min_total, manhattan_total(x, y, X, Y))
    return min_total


def manhattan_total(x, y, X, Y):
    total = 0
    for x1, y1 in zip(X, Y):
        total += abs(x1 - x) + abs(y1 - y)
    return total


if __name__ == "__main__":
    main()
