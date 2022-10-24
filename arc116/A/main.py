#!/usr/bin/env python3



def solve(T: int, case: "List[int]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    T = int(next(tokens))  # type: int
    case = [int(next(tokens)) for _ in range(T)]  # type: "List[int]"
    solve(T, case)


if __name__ == "__main__":
    main()
