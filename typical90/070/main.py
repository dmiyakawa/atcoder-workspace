#!/usr/bin/env python3


def manhattan_total(x, y, X, Y):
    total = 0
    for x1, y1 in zip(X, Y):
        total += abs(x1 - x) + abs(y1 - y)
    return total


def find_medianlike(lst: "List[int]") -> int:
    # 「中央値」は正確には偶数要素のときはさらに間の値を取る
    # ここでは単に中央値に一番近い要素のうち右側を取っている
    # e.g. 要素4ならソート後のindex 2の要素を返す
    # 左側を選ぶこともできるが、本問題では本質的に差はない
    sorted_ = sorted(lst)
    # 中央値の左側を採用する場合
    # return sorted_[len(lst)//2 - (1 if len(lst) % 2 == 0 else 0)]
    return sorted_[len(lst)//2]


def solve(N: int, X: "List[int]", Y: "List[int]"):
    return manhattan_total(find_medianlike(X), find_medianlike(Y), X, Y)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    print(solve(N, X, Y))


if __name__ == "__main__":
    main()
