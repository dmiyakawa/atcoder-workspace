#!/usr/bin/env python3

def solve_ref(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    """https://atcoder.jp/contests/abc147/submissions/36014055"""
    MAX = 80 * 160 + 5
    dp = [[0] * W for i in range(H)]
    dp[0][0] = 1 << (MAX + A[0][0] - B[0][0])
    dp[0][0] = 1 << (MAX + B[0][0] - A[0][0])
    for i in range(H):
        for j in range(W):
            d = abs(A[i][j] - B[i][j])
            if i:
                dp[i][j] |= dp[i - 1][j] << d
                dp[i][j] |= dp[i - 1][j] >> d
            if j:
                dp[i][j] |= dp[i][j - 1] << d
                dp[i][j] |= dp[i][j - 1] >> d

    ans = float("inf")
    for v in range(2 * MAX):
        if (dp[-1][-1] >> v) & 1:
            ans = min(ans, abs(v - MAX))
    print(ans)


def solve(H: int, W: int, A: "List[List[int]]", B: "List[List[int]]"):
    """一応AC。
    偏りは正負の差と考えて正負の区別を考えなくてよい
    するとそれぞれのマスでの値の差は最大で80、ステートは最大でも(79**2)*80にしかならない
    """
    possibles = [[set() for _ in range(W)] for _ in range(H)]
    possibles[0][0].add(abs(A[0][0] - B[0][0]))
    # possibles[0][0].add(B[0][0] - A[0][0])
    for h in range(H):
        for w in range(W):
            p = possibles[h][w]
            a = A[h][w]
            b = B[h][w]
            if h > 0:
                for prev in possibles[h - 1][w]:
                    p.add(abs(prev + a - b))
                    p.add(abs(prev + b - a))
            if w > 0:
                for prev in possibles[h][w - 1]:
                    p.add(abs(prev + a - b))
                    p.add(abs(prev + b - a))
    # print(possibles)
    print(min(abs(v) for v in possibles[H - 1][W - 1]))


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
    solve_ref(H, W, A, B)


def _debug():
    import random
    H, W = 80, 80
    A = [[random.randint(0, 80) for _ in range(W)] for _ in range(H)]
    B = [[0 for _ in range(W)] for _ in range(H)]
    # print(A)
    # print(B)
    solve(H, W, A, B)


if __name__ == "__main__":
    main()
    # _debug()
