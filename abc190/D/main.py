#!/usr/bin/env python3

def solve(N: int):
    """初AC https://atcoder.jp/contests/abc190/submissions/35196890
    解説とちょっと経路が違うので説明
    等差数列の和の公式からaを求めると a = (2*N - n**2 + n) / (2 * n)
    ここで、a <= 0 のときには a, ..., -1, 0, 1, ..., -a, -a + 1, ... という数列でなければ和は正の数Nには決してならず
    a 〜 -a の範囲は相殺されてしまうため -a + 1 以降の総和と値は同じ
    言い換えると
    a > 0 とした結果に加えて -a + 1, ..., 0, ..., a - 1, a, ... も解になる（なお、a == 1 のときも例の通り 0, 1）。
    つまり、正の整数 a が計算できる n が見つかるたびに解の個数は2増える
    aの分子についてnは2乗の速度で増えるので、O(√N)でこの探索は終わる（分子が負になり a > 0 の条件を満たせなくなる）
    """
    n = 1
    ans = 0
    while True:
        nmr = 2 * N - n**2 + n
        if nmr <= 0:
            break
        if nmr % (2 * n) == 0:
            ans += 2
        n += 1
    print(ans)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)




if __name__ == "__main__":
    main()
