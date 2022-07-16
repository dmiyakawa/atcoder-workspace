#!/usr/bin/env python3


def solve(H, W, S):
    # 回答例
    hs = [False for _ in range(H)]
    ws = [False for _ in range(W)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                hs[h] = True
                ws[w] = True

    for h in range(H):
        if hs[h]:
            print("".join(S[h][w] for w in range(W) if ws[w]))


def solve_0(H, W, S):
    # 初回実装
    deleted_rows = set()
    deleted_cols = set()
    while len(deleted_rows) < H and len(deleted_cols) < W:
        some_deleted = False
        for h in range(H):
            if h in deleted_rows:
                continue
            all_white = True
            for w in range(W):
                if w in deleted_cols:
                    continue
                if S[h][w] == "#":
                    all_white = False
                    break
            if all_white:
                some_deleted = True
                deleted_rows.add(h)
        for w in range(W):
            if w in deleted_cols:
                continue
            all_white = True
            for h in range(H):
                if h in deleted_rows:
                    continue
                if S[h][w] == "#":
                    all_white = False
                    break
            if all_white:
                some_deleted = True
                deleted_cols.add(w)
        if not some_deleted:
            break
    for h in range(H):
        if h in deleted_rows:
            continue
        print("".join(S[h][w] for w in range(W) if w not in deleted_cols))


def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)


if __name__ == "__main__":
    main()
