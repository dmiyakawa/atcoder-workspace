#!/usr/bin/env python3

def solve(N, M, K):
    for i in range(N + 1):
        for j in range(M + 1):
            if K == i * M + j * N - 2 * i * j:
                return True
    return False


def main():
    N, M, K = map(int, input().split())
    print("Yes" if solve(N, M, K) else "No")


if __name__ == "__main__":
    main()
