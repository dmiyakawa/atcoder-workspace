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
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    B = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A, B)


def solve(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    return


if __name__ == "__main__":
    main()
