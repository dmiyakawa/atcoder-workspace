#!/usr/bin/env python3


def main():
    N = int(input())
    M = int(input())
    K = [int(input()) for _ in range(M)]
    A = [n for n in range(1, N * 2 + 1)]
    for k in K:
        if k == 0:  # リフトシャッフル
            A = [A[i // 2] if i % 2 == 0 else A[N + i // 2] for i in range(2 * N)]
        else:
            A = A[k:] + A[:k]
    for a in A:
        print(a)


if __name__ == "__main__":
    main()
