#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


def solve(H: int, W: int, S: "List[str]"):
    dp = []
    for i in range(H):
        row = []
        dp.append(row)
        for j in range(W):
            is_b = S[i][j] == "#"
            if i > 0:
                n1, b1, w1 = dp[i - 1][j]
                is_prev_b = S[i - 1][j] == "#"
                if is_b:
                    if not is_prev_b:
                        n1 = w1
                    else:
                        n1 = set()
                        b1 = set()
                        w1 = set()
                else:
                    if is_prev_b:
                        n1 = b1
                    else:
                        n1 = set()
                        b1 = set()
                        w1 = set()
            else:
                n1, b1, w1 = set(), set(), set()
            if j > 0:
                n2, b2, w2 = dp[i][j - 1]
                is_prev_b = S[i][j - 1] == "#"
                if is_b:
                    if not is_prev_b:
                        n2 = w2
                    else:
                        n2 = set()
                        b2 = set()
                        w2 = set()
                else:
                    if is_prev_b:
                        n2 = b2
                    else:
                        n2 = set()
                        b2 = set()
                        w2 = set()
            else:
                n2, b2, w2 = set(), set(), set()
            # print(n1, n2, b1, b2, w1, w2)
            row.append((len(n1 | n2),
                        b1 | b2 | ({(i, j)} if is_b else set()),
                        w1 | w2 | (set() if is_b else {(i, j)})))
        # print(row)
    count = 0
    for i in range(H):
        count += sum(tup[0] for tup in dp[i])
    print(count)



def main():

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
