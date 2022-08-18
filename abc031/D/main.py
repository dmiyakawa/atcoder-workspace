#!/usr/bin/env python3
import copy


def search(V2, W, i, d):
    if i == len(V2):
        return d
    for d2 in gen(V2[i], W[i], 0, 0, d):
        ret = search(V2, W, i + 1, d2)
        if ret:
            return ret
    return None


def gen(lst, w, i, j, d):
    if (len(lst) - i) * 3 < len(w) - j:
        return
    if i == len(lst):
        if j == len(w):
            yield d
        return
    # print(lst[i:], w[j:], d)

    n = lst[i]
    if n in d:
        if d[n] != w[j:j + len(d[n])]:
            return
        yield from gen(lst, w, i + 1, j + len(d[n]), d)
    else:
        for l in range(1, 4):
            if j + l > len(w):
                break
            new_d = copy.copy(d)
            new_d[n] = w[j:j + l]
            yield from gen(lst, w, i + 1, j + l, new_d)


def solve(K: int, N: int, V: "List[int]", W: "List[str]"):
    V2 = []
    for v in V:
        lst = []
        while v:
            lst.append(v % 10)
            v //= 10
        V2.append(lst[::-1])
    d = search(V2, W, 0, {})
    for n in range(1, K + 1):
        print(d[n])

def solve_ref(K, N, V, W):
    """https://atcoder.jp/contests/abc031/submissions/33950273"""
    import itertools

    d = [(str(v), str(w)) for v, w in zip(V, W)]

    def chk(_pattern):
        _ans = {}
        for v, w in d:
            s, e = 0, 0
            for n in v:
                e += _pattern[int(n) - 1]
                txt = w[s:e]
                s += _pattern[int(n) - 1]
                if n not in _ans:
                    _ans[n] = txt
                elif _ans[n] != txt:
                    return None
        return _ans

    for pattern in itertools.product([1, 2, 3], repeat=K):
        for v, w in d:
            t = [pattern[int(n) - 1] for n in v]
            if sum(t) != len(w):
                break
        else:
            ans = chk(pattern)
            if ans:
                for n in range(1, K + 1):
                    print(ans[str(n)])
                return


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    v = [int()] * (N)  # type: "List[int]"
    w = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        v[i] = int(next(tokens))
        w[i] = next(tokens)
    solve_ref(K, N, v, w)


if __name__ == "__main__":
    main()
