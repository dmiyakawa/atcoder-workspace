#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = next(tokens)  # type: str
    x, y = 0, 0
    dx, dy = 1, 0
    for t in T:
        if t == "S":
            x, y = x + dx, y + dy
        else:
            if (dx, dy) == (1, 0):
                dx, dy = 0, -1
            elif (dx, dy) == (0, -1):
                dx, dy = -1, 0
            elif (dx, dy) == (-1, 0):
                dx, dy = 0, 1
            else:
                dx, dy = 1, 0
    print(x, y, end="")


if __name__ == "__main__":
    main()
