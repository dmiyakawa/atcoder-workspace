#!/usr/bin/env python3
from bisect import bisect


def solve(N: int, P: "List[int]"):
    s = []
    ans = None
    for i in range(N - 1, -1, -1):
        p = P[i]
        if i == N - 1:
            s.append(p)
            continue
        if s[-1] < p:
            s.reverse()
            # print(s, p)
            j = bisect(s, p)
            ans = P[:i]
            ans.append(s[j - 1])
            s[j - 1] = p
            s.reverse()
            ans.extend(s)
            break
        else:
            s.append(p)
    print(*ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)


if __name__ == "__main__":
    main()
