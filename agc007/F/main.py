#!/usr/bin/env python3



def solve(N: int, S: "List[str]", T: str):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(0 + 1)]  # type: "List[str]"
    T = next(tokens)  # type: str
    solve(N, S, T)


if __name__ == "__main__":
    main()
