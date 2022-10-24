#!/usr/bin/env python3



def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    rest = [1] * N
    wb = [False] * N
    wb[0] = True
    for x0, y0 in zip(x, y):
        x0 -= 1
        y0 -= 1
        rest[x0] -= 1
        rest[y0] += 1
        if wb[x0]:
            wb[y0] = True
        if rest[x0] == 0:
            wb[x0] = False
    print(wb.count(True))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)


if __name__ == "__main__":
    main()
