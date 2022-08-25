#!/usr/bin/env python3


def solve(H: int, W: int, S: "List[str]"):
    for i in range(H):
        S[i] = list(S[i])

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                continue
            count = 0
            for h, w in [
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j), (i, j + 1),
                (i + 1, j -1), (i + 1, j), (i + 1, j + 1)
            ]:
                if h < 0 or w < 0 or h >= H or w >= W:
                    continue
                if S[h][w] == "#":
                    count += 1
            S[i][j] = str(count)
    for h in range(H):
        print("".join(S[h]))


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == "__main__":
    main()
