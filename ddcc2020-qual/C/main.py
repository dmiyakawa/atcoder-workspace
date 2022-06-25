#!/usr/bin/env python3


def solve(H, W, K, grid):
    solve_ans1(H, W, K, grid)
    # solve_ans2(H, W, K, grid)
    # solve_mod(H, W, K, grid)


def solve_ans1(H, W, K, grid):
    # 公式解法1 ... 再帰的に解く
    import sys
    sys.setrecursionlimit(2 * (10 ** 5))

    nodes = []
    n = 0
    for i, line in enumerate(grid):
        for j, ch in enumerate(line):
            if ch == "#":
                n += 1
                nodes.append((i, j, n))

    ans = [[0 for _ in range(W)] for _ in range(H)]

    def _solve_inter(hu, hb, wl, wr, _ns):
        if len(_ns) == 1:
            val = _ns[0][2]
            for i in range(hu, hb):
                for j in range(wl, wr):
                    ans[i][j] = val
        else:
            if len({node[0] for node in _ns}) > 1:
                hs = sorted({node[0] for node in _ns})
                mid = hs[len(hs) // 2]
                next_ns_u = []
                next_ns_b = []
                for node in _ns:
                    if hu <= node[0] < mid:
                        next_ns_u.append(node)
                    else:
                        next_ns_b.append(node)
                _solve_inter(hu, mid, wl, wr, next_ns_u)
                _solve_inter(mid, hb, wl, wr, next_ns_b)
            else:
                ws = sorted({node[1] for node in _ns})
                mid = ws[len(ws) // 2]
                next_ns_l = []
                next_ns_r = []
                for node in _ns:
                    if wl <= node[1] < mid:
                        next_ns_l.append(node)
                    else:
                        next_ns_r.append(node)
                _solve_inter(hu, hb, wl, mid, next_ns_l)
                _solve_inter(hu, hb, mid, wr, next_ns_r)

    _solve_inter(0, H, 0, W, nodes)
    for lst in ans:
        print(*lst)


def solve_ans2(H, W, K, grid):
    # 公式解法2: 横に切って縦に切る
    groups = {}
    begin = 0
    last_key = None
    for h, line in enumerate(grid):
        group = [w for w, ch in enumerate(line) if ch == "#"]
        if group:
            last_key = (begin, h + 1)
            groups[last_key] = group
            begin = h + 1
    assert last_key
    if last_key[1] != H:
        groups[(last_key[0], H)] = groups[last_key]
        del groups[last_key]

    ans = [[0 for _ in range(W)] for _ in range(H)]
    n = 0
    for (u, b), group in groups.items():
        l = 0
        for k, w in enumerate(group):
            if k == len(group) - 1:
                w = W
            else:
                w += 1

            n += 1
            for i in range(u, b):
                for j in range(l, w):
                    ans[i][j] = n
            l = w

    for lst in ans:
        print(*lst)


def solve_mod(H, W, K, grid):
    # 公式解説解答例2に合わせてsolve_waを改修
    ss = []
    for h, line in enumerate(grid):
        for w, ch in enumerate(line):
            if ch == "#":
                ss.append((h, w))
    sss = [(h, w, n) for n, (h, w) in enumerate(sorted(ss, key=lambda tup: (h, w)), start=1)]
    ans = [[0 for _ in range(W)] for _ in range(H)]
    ssss = []
    for h, w, n in sss:
        ans[h][w] = n

    for h, w, n in sss:
        wl, wr = w, w + 1
        while True:
            if wl < 0 or ans[h][wl] not in [0, n]:
                wl += 1
                break
            wl -= 1
        while True:
            if wr == W or ans[h][wr] not in [0, n]:
                wr -= 1
                break
            wr += 1

        for w0 in range(wl, wr + 1):
            ans[h][w0] = n
        ssss.append((h, w, wl, wr, n))

    for h, w, wl, wr, n in ssss:
        hu, hb = h - 1, h + 1
        while True:
            if hu < 0 or ans[hu][w] not in [0, n]:
                hu += 1
                break
            hu -= 1

        while True:
            if hb >= H or ans[hb][w] not in [0, n]:
                hb -= 1
                break
            hb += 1

        for h0 in range(hu, hb + 1):
            for w0 in range(wl, wr + 1):
                ans[h0][w0] = n

    for lst in ans:
        print(*lst)


def solve_wa(H, W, K, grid):
    # ダメだったやつ
    ss = []
    for h, line in enumerate(grid):
        for w, ch in enumerate(line):
            if ch == "#":
                ss.append((h, w))
    sss = [(h, w, n) for n, (h, w) in enumerate(sorted(ss, key=lambda tup: (h, w)), start=1)]
    ans = [[0 for _ in range(W)] for _ in range(H)]
    for h, w, n in sss:
        ans[h][w] = n

    ssss = []
    for h, w, n in sss:
        hu = h
        wl = w
        while True:
            if hu < 0 or ans[hu][w] not in [0, n]:
                hu += 1
                break
            hu -= 1
        while True:
            if wl < 0 or any(ans[h0][wl] not in [0, n] for h0 in range(hu, h + 1)):
                wl += 1
                break
            wl -= 1

        for h0 in range(hu, h + 1):
            for w0 in range(wl, w + 1):
                ans[h0][w0] = n
        ssss.append((h, w, hu, wl, n))

    for h, w, hu, wl, n in ssss:
        hb = h
        wr = w
        while True:
            if hb >= H or any(ans[hb][w0] not in [0, n] for w0 in range(wl, w + 1)):
                hb -= 1
                break
            hb += 1

        while True:
            if wr >= W or any(ans[h0][wr] not in [0, n] for h0 in range(hu, hb + 1)):
                wr -= 1
                break
            wr += 1
        for h0 in range(hu, hb + 1):
            for w0 in range(wl, wr + 1):
                ans[h0][w0] = n


    for lst in ans:
        print(*lst)


def main():
    H, W, K = map(int, input().split())
    grid = []
    for h in range(H):
        grid.append(input())
    solve(H, W, K, grid)


def gen(H, W, K):
    import random
    assert 1 <= K <= H*W
    cand = [(i, j) for i in range(1, H + 1) for j in range(1, W + 1)]
    s = random.choices(cand, k=K)
    lst = []
    for i in range(1, H + 1):
        seq = [("#" if (i, j) in s else ".") for j in range(1, W + 1)]
        lst.append("".join(seq))
    return lst


def debug():
    H, W, K = 10, 10, 25
    grid = gen(H, W, K)
    print(H, W, K)
    for line in grid:
        print(line)
    solve(H, W, K, grid)


if __name__ == "__main__":
    main()
