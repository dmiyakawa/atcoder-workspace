#!/usr/bin/env python3

def main():
    """
    2022-07-26 に再チャレンジしてみた
    https://atcoder.jp/contests/abc246/submissions/33527777
    """
    N, K, X = map(int, input().split())
    A = [int(e) for e in input().split()]
    for i in range(N):
        k_used = min(A[i] // X, K)
        A[i] = A[i] - k_used * X
        K -= k_used
        if K == 0:
            break

    if K > 0:
        A.sort(reverse=True)
        for i in range(N):
            if K == 0:
                break
            A[i] = 0
            K -= 1

    print(sum(A))


if __name__ == "__main__":
    main()
