#!/usr/bin/env python3



def solve(N: int, K: int, A: "List[int]"):
    max_A = max(A)
    left, right = 0, max_A
    while right - left > 1:
        # m回回ったときにK個以上食べてますか
        m = (left + right) // 2
        c = 0
        for a in A:
            c += a if a < m else m
        if c >= K:
            right = m
        else:
            left = m
    # left回回ってもK個以上は食べていない。right回回るとK個以上食べている
    # -> left回回ってみる
    A0 = []
    for a in A:
        if a > left:
            A0.append(a - left)
            K -= left
        else:
            A0.append(0)
            K -= a
    assert K > 0
    # あと1回回る途中でK個食べきる
    ans = []
    for a in A0:
        if K == 0 or a == 0:
            ans.append(a)
        else:
            K -= 1
            ans.append(a - 1)

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
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == "__main__":
    main()
