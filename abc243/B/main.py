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
    solve(N, A, B)


def solve(N: int, A: "List[int]", B: "List[int]"):
    s_a = {}
    s_b = {}
    total_1 = 0
    for i in range(N):
        a, b = A[i], B[i]

        if a == b:
            total_1 += 1
        s_a[a] = s_a.get(a, 0) + 1
        s_b[b] = s_a.get(b, 0) + 1
    total_2 = 0
    for a in s_a:
        if a in s_b:
            total_2 += min(s_a[a], s_b[a])

    total_2 -= total_1
    print(total_1)
    print(total_2)


if __name__ == "__main__":
    main()
