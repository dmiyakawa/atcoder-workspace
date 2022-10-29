#!/usr/bin/env python3



def solve(N: int, v: "List[str]", w: "List[str]"):
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
    v = [str()] * (N - 1)  # type: "List[str]"
    w = [str()] * (N - 1)  # type: "List[str]"
    for i in range(N - 1):
        v[i] = next(tokens)
        w[i] = next(tokens)
    solve(N, v, w)


if __name__ == "__main__":
    main()
