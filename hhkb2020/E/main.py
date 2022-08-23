#!/usr/bin/env python3

MOD = 1000000007  # type: int


def solve(H: int, W: int, S: "List[str]"):
    """初AC\
    それぞれの散らかっていないマスについて、照らされるパターン数を求めて合計すると解になる

    各マスについて、照らされているパターンは「そのマスの照明がついているケース」と「ついていないケース」があり
    - そのマスの照明がついているケース * (2**(K - 1))
    - (2**そのマスを照らせる他の照明の数 - 1) * (2**そのマスに関係ない照明の数)
      - -1 は「照らせる全ての照明が消えているケース」。どれかついていれば良い

    以上で計算量はO(HW)だが、2**K が非常に大きくなった際にそれ自体の計算を繰り返してTLEするため
    2**i % MOD を事前に計算しておく
    """
    counts = [[0] * W for _ in range(H)]

    K = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                K += 1
    pcache = [1, 2]
    for _ in range(2, K + 1):
        pcache.append((pcache[-1] * 2) % MOD)

    for i in range(H):
        s = 0
        for j in range(W):
            if S[i][j] == "#":
                s = 0
            else:
                counts[i][j] += s
                s += 1
        s = 0
        for j in range(W - 1, -1, -1):
            if S[i][j] == "#":
                s = 0
            else:
                counts[i][j] += s
                s += 1

    for j in range(W):
        s = 0
        for i in range(H):
            if S[i][j] == "#":
                s = 0
            else:
                counts[i][j] += s
                s += 1
        s = 0
        for i in range(H - 1, -1, -1):
            if S[i][j] == "#":
                s = 0
            else:
                counts[i][j] += s
                s += 1
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans += pcache[K - 1]
                ans += (pcache[counts[i][j]] - 1) * (pcache[K - 1 - counts[i][j]])
                ans %= MOD

    print(ans % MOD)

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
