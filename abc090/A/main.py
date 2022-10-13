#!/usr/bin/env python3



def solve(c: "List[str]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    c = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(c)


if __name__ == "__main__":
    main()
