#!/usr/bin/env python3


def solve(N: int, K: int, S: str):
    """初AC
    - 同じ方向を向いている人の塊をセグメントと呼ぶことにする。セグメント数をnsとする
      - ns は、全員が同じ方向を向いているときを1として、1以上になる
    - セグメントごとに一人幸せでない人がいることから、幸福である人数は N - ns で計算できる
    - 「左右に他のセグメントがあるセグメント」を対象に回転をすると、nsは2つ減る。そうでないとき、nsは1つ減る
      - 例: >>><<>>> このケースでは左を向いている人のセグメントが「左右に他のセグメントがあるセグメント」
    - Kが許す限りセグメントを回転させられるわけだから、
    - できる限り「nsが2つ減る」回転を行い、最後の1回だけ「nsが1つ減る」回転をして、
    - 最後の ns を用いて N - ns を計算して回答とする
    """
    prev = None
    ns = 0
    for ch in S:
        if ch == prev:
            continue
        else:
            ns += 1
            prev = ch
    while K and ns > 1:
        if ns >= 3:
            ns = ns - 2
        else:
            ns = 1
        K -= 1
    print(N - ns)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)


if __name__ == "__main__":
    main()
