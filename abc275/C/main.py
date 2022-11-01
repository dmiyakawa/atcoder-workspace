#!/usr/bin/env python3



def solve(S: "List[str]"):
    ans = 0
    for h in range(9):
        for w in range(9):
            if S[h][w] != "#":
                continue
            for i in range(9):
                if h + i >= 9:
                    continue
                for j in range(9):
                    if i == 0 and j == 0:
                        continue
                    if w + i + j >= 9 or h + i + j >= 9:
                        continue
                    if S[h + i][w + j] != "#":
                        continue
                    if S[h + j][w + i] != "#":
                        continue
                    if S[h + i + j][w + i + j] != "#":
                        continue
                    ans += 1
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(9)]  # type: "List[str]"
    solve(S)


if __name__ == "__main__":
    main()
