#!/usr/bin/env python3

from typing import Optional, List

def search(prefix, _rem_S, _rem_us, _rem_T):
    if not _rem_T:
        if _rem_S:
            return prefix + "_" + "_".join(_rem_S)
        else:
            return prefix

    for s in _rem_S:
        next_rem_S = _rem_S - {s}
        for i in range(_rem_us + 1):
            cand = "{}{}{}".format(prefix, "_" * (i + 1), s)
            next_rem_T = []
            for _t in _rem_T:
                if _t.startswith(cand):
                    next_rem_T.append(_t)
            if not next_rem_T:
                if next_rem_S:
                    return cand + "_" + "_".join(next_rem_S)
                else:
                    return cand
            _ret = search(cand, next_rem_S, _rem_us - i, next_rem_T)
            if _ret and 3 <= len(_ret) <= 16:
                return _ret
    return None


def solve(N: int, M: int, S: "List[str]", T: "List[str]") -> Optional[str]:
    len_S_sum = sum([len(s) for s in S])
    rem_us = 16 - (len_S_sum + N - 1)
    assert rem_us >= 0

    set_S = set(S)
    for s in S:
        rem_T = []
        for t in T:
            if t.startswith(s):
                rem_T.append(t)
        ret = search(s, set_S - {s}, rem_us, rem_T)
        if ret and 3 <= len(ret) <= 16:
            return ret
    return None


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    T = [next(tokens) for _ in range(M)]  # type: "List[str]"
    ret = solve(N, M, S, T)
    print(ret if ret else -1)


if __name__ == "__main__":
    main()
