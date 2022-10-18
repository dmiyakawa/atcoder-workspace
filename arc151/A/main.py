#!/usr/bin/env python3
from collections import deque
from typing import Union


def solve(N: int, S: str, T: str):
    deq_s = deque()
    deq_t = deque()
    for i, (s, t) in enumerate(zip(S, T)):
        if s == t:
            continue
        if s == "1":
            if deq_t:
                deq_t.popleft()
            else:
                deq_s.append(i)
        else:
            assert t == "1"
            if deq_s:
                deq_s.popleft()
            else:
                deq_t.append(i)
    # print(deq_s, deq_t)
    ans: str
    if not deq_t and not deq_s:
        ans = "0" * N
    elif deq_s:
        if len(deq_s) % 2 == 1:
            ans = "-1"
        else:

            ss = set(list(deq_s)[len(deq_s) // 2:])
            ans = "".join("1" if i in ss else "0" for i in range(N))
    else:
        assert deq_t
        if len(deq_t) % 2 == 1:
            ans = "-1"
        else:
            ts = set(list(deq_t)[len(deq_t) // 2:])
            ans = "".join("1" if i in ts else "0" for i in range(N))
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(N, S, T)


if __name__ == "__main__":
    main()
