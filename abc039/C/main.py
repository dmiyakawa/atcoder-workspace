#!/usr/bin/env python3



def solve(S: str):
    i = ("WBWBWWBWBWBW" * 3).find(S[:12])
    lst = ["Do", None, "Re", None, "Mi", "Fa", None, "So", None, "La", None, "Si"]
    assert i >= 0
    print(lst[i])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
