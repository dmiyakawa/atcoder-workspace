#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    c = [next(tokens) for _ in range(1)]  # type: "List[str]"
    solve(N, c)


def solve(N: int, c: "List[str]"):
    return


if __name__ == "__main__":
    main()
