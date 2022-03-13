#!/usr/bin/env python3


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
    C = [[A[i][j] - B[i][j] for j in range(W)] for i in range(H)]
    count = 0
    possible = True
    for i in range(H - 1):
        for j in range(W - 1):
            val = C[i][j]
            if val != 0:
                count += abs(val)
                C[i][j] -= val
                C[i + 1][j] -= val
                C[i + 1][j + 1] -= val
                C[i][j + 1] -= val
        if C[i][W - 1] != 0:
            possible = False
            break
    if possible:
        for j in range(W):
            if C[H - 1][j] != 0:
                possible = False
            break
    print(f"Yes\n{count}" if possible else "No")


if __name__ == "__main__":
    main()
