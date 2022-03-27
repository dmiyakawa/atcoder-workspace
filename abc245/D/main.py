#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N + M + 1)]  # type: "List[int]"
    solve(N, M, A, C)


def solve(N: int, M: int, A: "List[int]", C: "List[int]"):
    # 1 <= N, 1 <= M
    B = []
    for m_i in range(0, N + M + 1):
        acc = 0
        final_ai = None
        for l in range(0, N + M + 1):
            if m_i - l >= len(A) or m_i - l < 0:
                continue
            if A[m_i - l] != 0:
                final_ai = m_i - l
            if l >= len(B):
                continue
            acc += A[m_i - l] * B[l]
        if final_ai is not None:
            b = (C[m_i] - acc) // A[final_ai]
            B.append(b)
        if len(B) == M + 1:
            break
    print(*B)


if __name__ == "__main__":
    main()
