#!/usr/bin/env python3


def solve(N: int, S: str):
    if list(S) == list(reversed(S)):
        return "Yes"
    if S == "BABB":
        return "Yes"
    if N > 4 and S[0] == S[N - 1] == "B":
        # BA(B*)BAB の形に必ず落とし込める
        return "Yes"
    for i in range(N // 2):
        if S[N - i - 1] == "A" and (N % 2 == 1 or i < N // 2 - 1):
            break
        elif S[i] == S[N - i - 1]:
            continue
        else:
            return "No"
    return "Yes"


def main():
    N = int(input())
    S = input()
    print(solve(N, S))


def _debug():
    for N in range(2, 8):
        for v in range(2**N):
            S = "".join("A" if v >> i & 1 else "B" for i in range(N))
            print(N, S, solve(N, S))


if __name__ == "__main__":
    # _debug()
    main()

