#!/usr/bin/env python3


def solve(H: int, W: int, N: int, R: "List[int]", C: "List[int]", A: "List[int]"):
    """ 解説と本質的には同じ https://atcoder.jp/contests/abc224/editorial/2814 """
    moves = [0 for _ in range(N)]
    rows = [-1 for _ in range(H)]
    cols = [-1 for _ in range(W)]
    pieces = sorted(((a, i) for i, a in enumerate(A)), reverse=True)
    prev = None
    prevs = []
    for j, (a, i) in enumerate(pieces):
        r, c = R[i] - 1, C[i] - 1

        if prev is not None and prev != a:
            for (prev_i, prev_r, prev_c, prev_v) in prevs:
                moves[prev_i] = prev_v
                rows[prev_r] = max(rows[prev_r], prev_v)
                cols[prev_c] = max(cols[prev_c], prev_v)

        if j == 0:
            v = 0
        else:
            v = max(rows[r], cols[c]) + 1
        if prev != a:
            prev = a
            prevs = [(i, r, c, v)]
        else:
            prevs.append((i, r, c, v))

    for (prev_i, prev_r, prev_c, prev_v) in prevs:
        moves[prev_i] = prev_v

    for i in range(N):
        print(moves[i])


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    r = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    a = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(H, W, N, r, c, a)


if __name__ == "__main__":
    main()
