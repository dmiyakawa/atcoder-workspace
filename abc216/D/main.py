#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    E = []
    for _ in range(M):
        k = int(input())
        lst = list(map(int, input().split()))
        for i in range(k - 1):
            E.append((lst[i] - 1, lst[i + 1] - 1))
    ans, _ = topological_sort_kahn(N, E)
    print(YES if len(ans) == N else NO)


def topological_sort_kahn(N, E: "List[Tuple[int, int]]") -> "Tuple[List[int], bool]":
    """トポロジカルソートの結果と、その結果が一意であるかを示すフラグをタプルで返す。
    ノード番号は [0, N-1]
    「Kahnのアルゴリズム」と呼ばれるアルゴリズム
    """
    from collections import deque

    G = [[] for _ in range(N)]
    C = [0] * N

    for i, j in E:
        G[i] += j,
        C[j] += 1

    q = deque(i for i in range(N) if not C[i])
    is_unique = True
    ans = []
    while q:
        if 1 < len(q):
            is_unique = False
        i = q.popleft()
        ans.append(i)
        for j in G[i]:
            C[j] -= 1
            if not C[j]:
                q += j,
    return ans, is_unique


def main_ref():
    """https://atcoder.jp/contests/abc216/editorial/2559
    - 便宜的に色番号を示す値は1〜Nではなく0〜N-1とする
    - 各色番号について、その色のぼーるを一番上に持つ筒へのインデックス [0, M - 1] のリストを indices に持つ
      - 問題の制約から、各色番号についてのリストサイズは0, 1, 2のどれかである
      - 2ということは「筒2つについて、一番上のボールの色が揃っている」ことがわかる
    - 入力を受け取ったあと構築した筒（リスト）のリストを As とする
      - それぞれの筒は末尾を先頭にするように入力のリストをひっくり返す。取り出す pop() 操作をO(1)で行うため
    - Asを構築したあと、まずそれぞれの筒の一番上のボールの色から最初の indices を構築する
      - この際、リストの長さが2となる色について、その色のボールを持つ筒番号 ([0, M-1]) を stack に置く
      - 元の解説ではここqueになっているがわざわざdequeを持ち込むのも面倒なのでstack（リスト）とした。順序のないsetであっても解ける
    - stack が空になるまで、以下を行う
      - まずstackの先頭を取り出し、その筒番号の先頭を取り除く。なぜなら、「色の同じボールが2個揃っている」状態であるからである
      - その上で、その筒番号にボールがあるようなら、その先頭を見て indices にその情報を加える
      - もし上の情報追加でその色番号のリストサイズが 2 になるようなら、stack に2つの筒番号を足す
    - 上記を繰り返すと、以下のどちらかになる
      1. もし当該の操作ができるなら、すべての筒が空になるまで、stackには新しい筒番号が追加されるはずである
      2. もし当該の操作が出来ないなら、indicesにリスト長が 2 となる色番号がなくなり、筒のボールを消費する前にstackが空になる
    """
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    As = []
    for _ in range(M):
        input()
        As.append([int(e) - 1 for e in input().split()][::-1])

    # [0, N-1]
    indices = [[] for _ in range(N)]
    stack = []
    for i, A in enumerate(As):
        v = A[-1]
        indices[v].append(i)
        if len(indices[v]) == 2:
            stack.extend(indices[v])
    while stack:
        i = stack.pop()
        As[i].pop()
        if As[i]:
            v = As[i][-1]
            indices[v].append(i)
            if len(indices[v]) == 2:
                stack.extend(indices[v])
    print(NO if any(A for A in As) else YES)


if __name__ == "__main__":
    main()
    # main_ref()
