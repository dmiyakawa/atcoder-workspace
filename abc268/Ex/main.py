#!/usr/bin/env python3



def solve(S: str, N: int, T: "List[str]"):
    return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    N = int(next(tokens))  # type: int
    T = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(S, N, T)


if __name__ == "__main__":
    main()
