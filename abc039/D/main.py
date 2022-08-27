#!/usr/bin/env python3


def solve(H: int, W: int, S: "List[str]"):
    lst = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            all_black = True
            for i0, j0 in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                           (i, j - 1), (i, j), (i, j + 1),
                           (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= i0 < H and 0 <= j0 < W:
                    if S[i0][j0] == ".":
                        all_black = False
                        break
                if not all_black:
                    break
            if all_black:
                lst[i][j] = True

    lst2 = [["."] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                possible = False
                for i0, j0 in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                               (i, j - 1), (i, j), (i, j + 1),
                               (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= i0 < H and 0 <= j0 < W and lst[i0][j0]:
                        possible = True
                        break
                if not possible:
                    print("impossible")
                    return
            if lst[i][j]:
                lst2[i][j] = "#"

    print("possible")
    for row in lst2:
        print("".join(row))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

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
