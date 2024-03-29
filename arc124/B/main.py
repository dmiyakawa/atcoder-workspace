#!/usr/bin/env python3



def solve(N: int, A: "List[int]", B: "List[int]"):
    for i in range(B):
        cand = A[0] ^ B[i]
        used = [False] * N
        used[i] = True



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, b)


if __name__ == "__main__":
    main()
