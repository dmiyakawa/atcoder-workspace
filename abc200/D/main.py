#!/usr/bin/env python3


def solve(N, A):
    import itertools
    reachables = {}
    A_mod = []
    for i, a in enumerate(A):
        A_mod.append(a % 200)

    # 一見無理筋な組み合わせ数だが、reachablesのkey数が最大200しか育たないのでかなり高速にサチる
    # サチるまで組み合わせを試せば良い
    for n in range(1, N + 1):
        for tup in itertools.combinations(range(N), n):
            val = sum(A_mod[i] for i in tup) % 200
            if val in reachables and reachables[val] != tup:
                return reachables[val], tup
            reachables[val] = tup
    return None


def main():
    N = int(input())
    A = [int(e) for e in input().split()]

    ret = solve(N, A)
    if ret:
        print("Yes")
        print(len(ret[0]), *sorted(i + 1 for i in ret[0]))
        print(len(ret[1]), *sorted(i + 1 for i in ret[1]))
    else:
        print("No")


if __name__ == "__main__":
    main()
