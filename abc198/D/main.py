#!/usr/bin/env python3

import sys
from typing import List

sys.setrecursionlimit(2 * (10 ** 5))


def solve_ref(S: "List[str]"):
    """\
    解説の実装。ほぼ全探索
    https://atcoder.jp/contests/abc198/editorial/1050
    制限時間5secに対してPyPy3でも3秒超かかる。ループ内で手を抜くとTLE
    """
    import itertools

    s = set(S[0] + S[1] + S[2])
    if len(s) >= 11:
        print("UNSOLVABLE")
        return
    d = {ch: i for i, ch in enumerate(sorted(s))}
    for perm in itertools.permutations(range(10), len(s)):
        if perm[d[S[0][0]]] * perm[d[S[1][0]]] * perm[d[S[2][0]]] == 0:
            continue
        n = [0, 0, 0]
        for i in range(3):
            for k in range(len(S[i])):
                n[i] += perm[d[S[i][-k - 1]]] * 10 ** k
        if n[0] + n[1] == n[2]:
            print(*n, sep="\n")
            return
    print("UNSOLVABLE")


def calc_alphametic(A, B, C, possibles, i, carry):
    """\
    初AC時の実装。正面から覆面算を解いた
    https://atcoder.jp/contests/abc198/submissions/33711043
    """
    if i >= max(len(A), len(B), len(C)):
        if carry > 0:
            return None
        va = sum(next(iter(possibles[v])) * 10**i for i, v in enumerate(A))
        vb = sum(next(iter(possibles[v])) * 10**i for i, v in enumerate(B))
        vc = sum(next(iter(possibles[v])) * 10**i for i, v in enumerate(C))
        if va == 0 or vb == 0 or vc == 0:
            return None
        return va, vb, vc

    for ap in possibles[A[i]] if i < len(A) else {-1}:
        if i >= len(B):
            bas = {-1}
        elif i < len(A) and B[i] == A[i]:
            bas = {ap}
        else:
            bas = possibles[B[i]] - {ap}

        for bp in bas:
            if i >= len(C):
                cas = {-1}
            elif i < len(A) and C[i] == A[i]:
                cas = {ap}
            elif i < len(B) and C[i] == B[i]:
                cas = {bp}
            else:
                cas = possibles[C[i]] - {ap, bp}

            for cp in cas:
                apt = ap if ap >= 0 else 0
                bpt = bp if bp >= 0 else 0
                cpt = cp if cp >= 0 else 0
                if (apt + bpt + carry) % 10 != cpt:
                    continue
                next_carry = (apt + bpt + carry) // 10
                new_possibles = []
                for j, p in enumerate(possibles):
                    if i < len(A) and j == A[i]:
                        new_possibles.append({ap})
                    elif i < len(B) and j == B[i]:
                        assert bp in p
                        new_possibles.append({bp})
                    elif i < len(C) and j == C[i]:
                        assert cp in p
                        new_possibles.append({cp})
                    else:
                        to_remove = {p for p in [ap, bp, cp] if p >= 0}
                        new_possibles.append(p - to_remove)

                ret = calc_alphametic(A, B, C, new_possibles, i + 1, next_carry)
                if ret:
                    return ret
    return None


def solve(S: "List[str]"):
    A = [ord(ch) - ord("a") for ch in reversed(S[0])]
    B = [ord(ch) - ord("a") for ch in reversed(S[1])]
    C = [ord(ch) - ord("a") for ch in reversed(S[2])]
    possibles = [{j for j in range(10)} if i in set(A + B + C) else set() for i in range(26)]
    possibles[A[-1]].discard(0)
    possibles[B[-1]].discard(0)
    possibles[C[-1]].discard(0)
    ret = calc_alphametic(A, B, C, possibles, 0, 0)
    if ret:
        print(ret[0])
        print(ret[1])
        print(ret[2])
    else:
        print("UNSOLVABLE")


def main():
    S = [input() for _ in range(3)]
    solve_ref(S)


if __name__ == "__main__":
    main()
