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
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    AX = [int()] * (N)  # type: "List[int]"
    AY = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        AX[i] = int(next(tokens))
        AY[i] = int(next(tokens))
    BX = [int()] * (N)  # type: "List[int]"
    BY = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        BX[i] = int(next(tokens))
        BY[i] = int(next(tokens))
    solve(N, T, AX, AY, BX, BY)


def solve(N: int, T: int, AX: "List[int]", AY: "List[int]", BX: "List[int]", BY: "List[int]"):
    return


if __name__ == "__main__":
    main()
