#!/usr/bin/env python3

def solve(N, A):
    solve_2(N, A)
    # solve_org(N, A)



def solve_org(N, A):
    """\
    初ACのもの。本質的には公式の解説とおなじことをしている
    ただし、1.5secくらいかかっており、速度的には 2sec 制限にたいしてはギリギリ。胃がキリキリ。
    定数倍単位で遅さが目立つのはジェネレータが原因
    """
    MAX = 2 ** (2 * N) - 1

    def gen_comb(used, score):
        if used == MAX:
            yield score
        else:
            for i in range(2 * N):
                if (1 << i) & used:
                    continue
                for j in range(i + 1, 2 * N):
                    if (1 << j) & used:
                        continue
                    yield from gen_comb(used | 1 << i | 1 << j, score ^ A[i][j])
                break

    print(max(score for score in gen_comb(0, 0)))


def solve_2(N, A):
    """\
    solve_org()をベースにしてジェネレータをやめたもの
    453 msでジェネレータ版よりも数倍高速
    """
    MAX = 2 ** (2 * N) - 1

    max_score = 0

    def solve_inter(used, score):
        nonlocal max_score
        if used == MAX:
            max_score = max(max_score, score)
        else:
            for i in range(2 * N):
                if (1 << i) & used:
                    continue
                for j in range(i + 1, 2 * N):
                    if (1 << j) & used:
                        continue
                    solve_inter(used | 1 << i | 1 << j, score ^ A[i][j])
                break

    solve_inter(0, 0)
    print(max_score)


def solve_3(N, A):
    """\
    solve_3()で整数で管理していたところを集合にしたもの。
    1363 msとだいぶ遅くなる
    https://atcoder.jp/contests/abc236/submissions/33881396
    """
    max_score = 0

    def solve_inter(used, score):
        nonlocal max_score
        if len(used) == 2 * N:
            max_score = max(max_score, score)
        else:
            for i in range(2 * N):
                if i in used:
                    continue
                for j in range(i + 1, 2 * N):
                    if j in used:
                        continue
                    solve_inter(used | {i, j}, score ^ A[i][j])
                break

    solve_inter(set(), 0)
    print(max_score)


def solve_ref(N, A):
    """\
    https://atcoder.jp/contests/abc236/submissions/33828050
    相対的に数倍高速。solve_2()のアイディアの元
    """
    ans = 0

    def dfs(lst, score):
        nonlocal ans

        if not lst:
            ans = max(ans, score)
            return
        x = lst[0]
        for i in range(1, len(lst)):
            y = lst[i]
            nxt = lst[1:i] + lst[i + 1:]
            dfs(nxt, score ^ A[x - 1][y - 1])

    all_list = [i + 1 for i in range(2 * N)]
    dfs(all_list, 0)
    print(ans)


def main():
    N = int(input())
    A = [[0 for _ in range(2 * N)] for _ in range(2 * N)]
    for i in range(2 * N - 1):
        lst = [int(e) for e in input().split()]
        for k, j in enumerate(range(i + 1, 2 * N)):
            A[i][j] = lst[k]
            A[j][i] = lst[k]
    solve(N, A)


def _debug(N=8):
    import random
    A = [[0 for _ in range(2 * N)] for _ in range(2 * N)]
    for i in range(2 * N):
        for j in range(i + 1, 2 * N):
            A[i][j] = A[j][i] = random.randint(0, 10**30)
    solve(N, A)


if __name__ == "__main__":
    # _debug()
    main()

