#!/usr/bin/env python3

def solve(N: int, S: str):
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    for i in range(1, N + 1):
        L[i] = L[i - 1] + (1 if S[i - 1] == "#" else 0)
    for i in range(N - 1, -1, -1):
        R[i] = R[i + 1] + (1 if S[i] == "." else 0)
    ans = N
    for i in range(N + 1):
        ans = min(ans, L[i] + R[i])
    print(ans)


def main():
    N = int(input())  # type: int
    S = input().rstrip()  # type: str
    if N == 0:  # For debugging
        N = len(S)
    solve(N, S)


if __name__ == "__main__":
    main()
