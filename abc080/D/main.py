#!/usr/bin/env python3



def solve(N: int, C: int, s: "List[int]", t: "List[int]", c: "List[int]"):
    max_t = max(t)
    lst = [0] * (max_t + 2)
    d = {}
    for t0, s0, c0 in sorted(zip(t, s, c)):
        s0 -= 1
        t0 -= 1
        if (s0, c0) in d:
            d[(t0, c0)] = d[(s0, c0)]
            del d[(s0, c0)]
        else:
            d[(t0, c0)] = s0
    for (t0, _), s0 in d.items():
        lst[s0] += 1
        lst[t0 + 1] -= 1
    acc = 0
    ans = 0
    for v in lst:
        acc += v
        ans = max(ans, acc)
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
    C = int(next(tokens))  # type: int
    s = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, s, t, c)


if __name__ == "__main__":
    main()
