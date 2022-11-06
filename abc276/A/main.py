#!/usr/bin/env python3



def solve(S: str):
    for i in range(len(S) - 1, -1, -1):
        if S[i] == "a":
            print(i + 1)
            return
    print(-1)


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
