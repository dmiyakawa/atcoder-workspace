#!/usr/bin/env python3


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]"):
    import bisect
    Ac = A.copy()
    Bc = B.copy()
    for i in range(1, N):
        Ac[i] += Ac[i - 1]
    for i in range(1, M):
        Bc[i] += Bc[i - 1]
    num_a = bisect.bisect_right(Ac, K)
    K_a = K - (0 if num_a == 0 else Ac[num_a - 1])
    num_b = bisect.bisect_right(Bc, K_a)
    K_rem = K_a - (0 if num_b == 0 else Bc[num_b - 1])
    num_max = num_a + num_b
    while num_a > 0 and num_b < M:
        K_rem += Ac[num_a - 1] - (0 if num_a == 1 else Ac[num_a - 2])
        num_a -= 1
        while True:
            if num_b >= M:
                break
            req = Bc[num_b] - (0 if num_b == 0 else Bc[num_b - 1])
            if req > K_rem:
                break
            K_rem -= req
            num_b += 1
        num_max = max(num_max, num_a + num_b)
    print(num_max)


def main():
    N, M, K = map(int, input().split())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    solve(N, M, K, A, B)


if __name__ == "__main__":
    main()
