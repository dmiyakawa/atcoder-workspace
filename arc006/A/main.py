#!/usr/bin/env python3



def solve(E: "List[int]", B: int, L: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    E = [int(next(tokens)) for _ in range(5 + 1)]  # type: "List[int]"
    B = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(5 + 1)]  # type: "List[int]"
    solve(E, B, L)


if __name__ == "__main__":
    main()
