#!/usr/bin/env python3


def solve(N: int, A: "List[int]"):
    """初ACのもの
    - 10**9だと30bitくらい要る。2進数の各桁ごとに考える
    - 各桁について、xorの結果は当然0, 1の2つに分かれる。これをgroup[0], group[1]としてリストにする
    - 全ての結果が片方によっている場合、Nが偶数であることからxorの対象は奇数で、1なら全ビットが1, 0なら全ビットが0
      - ちなみに書いていて気づいたけど、これは「下の結果の特別な例」なので要らない分岐だった……
    - group[0] と group[1] の両方に結果が分かれている場合、Nは偶数名ので両方のグループのメンバ数は偶奇は一致する
    - グループが偶数個ずつに分割されている場合、group[1]の結果は「自分が1であること」を意味している（自分を除くと個数が奇数であることに注目）
    - グループが奇数個ずつに分割されている場合、group[0]の結果は「自分が1であること」を意味している（group[1]の個数が奇数であることに注目）
    """
    NUM_BITS = 32
    groups = [[[], []] for _ in range(NUM_BITS)]
    for i in range(N):
        for b in range(NUM_BITS):
            groups[b][A[i] >> b & 1].append(i)

    B = [0] * N
    for b in range(NUM_BITS):
        group = groups[b]
        if len(group[0]) == 0:
            for i in range(N):
                B[i] |= 1 << b
        elif len(group[1]) == 0:
            pass
        else:
            if len(group[0]) % 2 == 0:
                for i in group[1]:
                    B[i] |= 1 << b
            else:
                for i in group[0]:
                    B[i] |= 1 << b

    # from functools import reduce
    # print("org", *A)
    # print("xor", *[reduce(lambda x, y: x ^ y, B[:i] + B[i + 1:]) for i in range(N)])
    print(*B)


def solve_ref(N: int, A: "List[int]"):
    """https://img.atcoder.jp/abc171/editorial.pdf"""
    from functools import reduce
    S = reduce(lambda x, y: x^y, A)
    print(*[S ^ a for a in A])


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_ref(N, a)


if __name__ == "__main__":
    main()
