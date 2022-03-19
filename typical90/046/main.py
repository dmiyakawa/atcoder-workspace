#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    Am, Bm, Cm = {}, {}, {}
    for a, b, c in zip(A, B, C):
        Am[a % 46] = Am.get(a % 46, 0) + 1
        Bm[b % 46] = Bm.get(b % 46, 0) + 1
        Cm[c % 46] = Cm.get(c % 46, 0) + 1
    count = 0
    for a in range(0, 46):
        for b in range(0, 46):
            for c in range(0, 46):
                if (a + b + c) % 46 == 0:
                    count += Am.get(a, 0) * Bm.get(b, 0) * Cm.get(c, 0)
    print(count, end="")


if __name__ == "__main__":
    main()
