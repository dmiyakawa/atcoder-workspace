#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    x = [int()] * (4)  # type: "List[int]"
    y = [int()] * (4)  # type: "List[int]"
    for i in range(4):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(x, y)


def solve(x: "List[int]", y: "List[int]"):
    return


if __name__ == "__main__":
    main()
