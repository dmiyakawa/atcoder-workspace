#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, P, Y)


def solve(N: int, M: int, P: "List[int]", Y: "List[int]"):
    d = {}
    ans = {}
    # index mの市(y年誕生、p県に属する)としたとき、市をyでソート
    for y, m, p in sorted([(y, m, p) for m, (y, p) in enumerate(zip(Y, P))]):
        tmp = d.setdefault(p, {})
        tmp[m] = len(tmp) + 1
        ans[m] = f"{p:06d}{tmp[m]:06d}"

    for i in range(M):
        print(ans[i])


if __name__ == "__main__":
    main()
