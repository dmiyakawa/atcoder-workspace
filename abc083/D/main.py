#!/usr/bin/env python3



def solve(S: str):
    lst1 = []
    prev_ch = None
    prev_len = None
    total = 0
    for s in S:
        if prev_ch != s:
            if prev_ch is not None:
                total += prev_len
                lst1.append((prev_ch, prev_len, total))
            prev_ch = s
            prev_len = 1
        else:
            prev_len += 1
    if prev_ch:
        total += prev_len
        lst1.append((prev_ch, prev_len, total))
    ans = 0
    lst2 = list(reversed(lst1))
    N = len(lst1)
    for i in range(N):
        if i == 0 or i == N - 1:
            ans = max(ans, lst1[i][1])
        else:
            if lst1[i - 1][2] >= lst1[i + 1][1]:
                l = lst1[i][2]
            else:
                l = lst1[i + 1][1]


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
