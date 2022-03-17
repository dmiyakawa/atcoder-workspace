#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve(a, b, c)


def solve(a: int, b: int, c: int):
    print(YES if a < c ** b else NO, end="")


def solve_wrong(a: int, b: int, c: int):
    # 誤差が発生してWAが出る実装。サンプルとして実際のテストデータからin_ex_1.txtとout_ex_1.txtも付属
    import math
    print(YES if math.log2(a) < b * math.log2(c) else NO, end="")


if __name__ == "__main__":
    main()
