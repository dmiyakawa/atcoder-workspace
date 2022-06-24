#!/usr/bin/env python3

import math

Inf = INF = float("INF")


def main():
    N, H = map(int, input().split())
    # 1 <= C < A <= 10**6
    # 1 <= D < B <= 10**6
    A, B, C, D, E = map(int, input().split())
    # H - E*N + (B + E)*a + (D + E)*b >= 0, N >= a >= 0, N >= b >= 0 の元、
    # 最小化: A*a + C*b
    current_min = Inf
    # current_b = None
    for b in range(N + 1):
        a = math.ceil(max(E * N - (D + E) * b - H, 0) / (B + E))

        if H - E*N + (B + E)*a + (D + E)*b <= 0 or a + b > N:
            continue
        if A * a + C * b <= current_min:
            current_min = A * a + C * b
            # current_b = b
    print(current_min)


if __name__ == "__main__":
    main()
