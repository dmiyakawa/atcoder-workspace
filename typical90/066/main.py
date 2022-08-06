#!/usr/bin/env python3


def solve(N: int, L: "List[int]", R: "List[int]"):
    dp = [[0 for _ in range(M)] for _ in range(N)]
    return



def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, L, R)




if __name__ == "__main__":
    main()
