#!/usr/bin/env python3


def solve(N: int, M: int, A: "List[int]"):
    B = [set() for _ in range(M + 1)]
    max_v = 0
    for v in range(N + 1):  # v になることはあるのか。それは第m回目のときか
        v_happens = False
        for i, a in enumerate(A):
            if a > v:  # 開始時に v より大きいなら、vには絶対ならない
                continue
            if (v - a) % (i + 1):
                continue
            m = (v - a) // (i + 1)
            if m > M:
                continue
            # 第m回目にvになる項がある
            B[m].add(v)  # type: ignore
            v_happens = True
        # vが起こる
        if not v_happens:
            break
        max_v = v
    # print(B)
    # print(max_v)
    # print("--")
    for m in range(1, M + 1):
        b = B[m]
        ans = 0
        for v in range(max_v + 1):
            if v not in b:
                break
            ans = v + 1
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
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == "__main__":
    main()
