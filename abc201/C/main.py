#!/usr/bin/env python3


def solve_2(S: str):
    # 解説読後
    included = set()
    excluded = set()
    assert len(S) == 10
    for i, ch in enumerate(S):
        if ch == "o":
            included.add(i)
        elif ch == "x":
            excluded.add(i)
    count = 0
    for n in range(10000):
        to_be_included = included.copy()
        ok = True
        for ch in f"{n:04d}":
            v = int(ch)
            to_be_included.discard(v)
            if v in excluded:
                ok = False
                break
        if to_be_included:
            ok = False
        if ok:
            count += 1
    return count


def comb(n, r):
    """nCr を計算する。 factorial(N) // factorial(N - r) // factorial(r) より概して高速"""
    from operator import mul
    from functools import reduce
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def solve(S: str):
    # 失敗例確認付き初コミット……
    included = set()
    excluded = set()
    not_sure = set()
    assert len(S) == 10
    for i, ch in enumerate(S):
        if ch == "o":
            included.add(i)
        elif ch == "x":
            excluded.add(i)
        else:
            not_sure.add(i)
    ni = len(included)
    nn = len(not_sure)
    if ni >= 5:
        return 0
    elif ni == 4:
        ret = 4 * 3 * 2
    elif ni == 3:
        # not_sureから1種類で4種類を 4!
        ret = 0
        if nn >= 1:
            ret += nn * 4 * 3 * 2
        # 1231, 1232, 1233
        ret += 3 * 4 * 3
    elif ni == 2:
        ret = 0
        if nn >= 2:
            # 12nm
            ret += comb(nn, 2) * 4 * 3 * 2
        if nn >= 1:
            # 121n, 122n, 12nn
            ret += nn * 3 * 4 * 3
        # e.g.
        # 1133, 1313, 1331, 3311, 3113, 3131
        # 1113, 1131, 1311, 3111
        ret += 2 * 3 + 4 * 2
    elif ni == 1:
        ret = 0
        if nn >= 3:
            ret += comb(nn, 3) * 4 * 3 * 2
        if nn >= 2:
            # 11nm, 1nnm, 1mnm
            ret += comb(nn, 2) * 3 * 4 * 3
        if nn >= 1:
            # 111n, 11nn, 1nnn
            ret += nn * (4 + 2 * 3 + 4)
        ret += 1
    else:
        if nn == 0:
            return 0
        ret = 0
        if nn >= 4:
            ret += comb(nn, 4) * 4 * 3 * 2
        if nn >= 3:
            ret += comb(nn, 3) * 3 * 4 * 3
        if nn >= 2:
            # nmmm, nnmm, nnnm
            ret += comb(nn, 2) * (4 + 6 + 4)
        ret += nn

    return ret


def main():
    print(solve_2(input()))


if __name__ == "__main__":
    main()
