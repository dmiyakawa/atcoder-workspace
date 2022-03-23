#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(A)


def solve(A: "List[int]"):
    return


if __name__ == "__main__":
    main()
