#!/usr/bin/env python3



def solve(M: "List[int]", D: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    M = [int()] * (2)  # type: "List[int]"
    D = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        M[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(M, D)


if __name__ == "__main__":
    main()
