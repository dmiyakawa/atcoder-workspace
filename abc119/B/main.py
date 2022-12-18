#!/usr/bin/env python3



def solve(N: int, x: "List[float]", u: "List[str]"):
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
    x = [float()] * (N)  # type: "List[float]"
    u = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        x[i] = float(next(tokens))
        u[i] = next(tokens)
    solve(N, x, u)


if __name__ == "__main__":
    main()
