#!/usr/bin/env python3

MOD = 998244353  # type: int


def solve(N: int, M: int, Q: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    for a, b, c, d in zip(A, B, C, D):
        ans = 0
        h = b - a + 1
        w = d - c + 1
        odd_start = (a + c) % 2 == 1
        odd_end = (b + c) % 2 == 1
        a_even, a_odd = (a + 1, a) if odd_start else (a, a + 1)
        b_even, b_odd = (b - 1, b) if odd_end else (b, b - 1)

        w_even = w // 2 + w % 2
        w_odd = w - w_even
        h_even = (b_even - a_even) // 2 + 1
        h_odd = h - h_even

        s_even = w_even * (c + (d if w % 2 else d - 1)) // 2
        s_odd = w_odd * (c + 1 + (d - 1 if w % 2 else d)) // 2

        m_even = w_even * (h_even * (2 * (a_even - 1) * M + (h_even - 1) * 2 * M)) // 2
        m_odd = w_odd * (h_odd * (2 * (a_odd - 1) * M + (h_odd - 1) * 2 * M)) // 2

        ans_even = s_even * h_even + m_even
        ans += ans_even
        ans %= MOD
        ans_odd = s_odd * h_odd + m_odd
        ans += ans_odd
        ans %= MOD
        # print(f"a: {a}, b: {b}, c: {c}, d: {d}")
        # print(f"a_even: {a_even}, b_even: {b_even}")
        # print(f"h_even: {h_even}, w_even: {w_even}, h_odd: {h_odd}, w_odd: {w_odd}")
        # print(f"s_even: {s_even}, m_even: {m_even}")
        # print(f"s_odd: {s_odd}, m_odd: {m_odd}")
        # print(f"ans_even: {ans_even}, ans_odd: {ans_odd}")
        print(ans)
        # print()


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    C = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, Q, A, B, C, D)


if __name__ == "__main__":
    main()
