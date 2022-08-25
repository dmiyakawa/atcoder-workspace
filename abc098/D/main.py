#!/usr/bin/env python3

def solve(N: int, A: "List[int]"):
    M = 20
    B = [0] * M
    l, r = 0, 1
    ans = 0
    for i in range(M):
        B[i] = A[0]>>i & 1
    while l < r <= N:
        while r < N:
            ans += r - l
            for i in range(M):
                B[i] += A[r]>>i & 1
            r += 1
            if not all(B[i] <= 1 for i in range(M)):
                break
        if r == N:
            break
        while l < r:
            for i in range(M):
                B[i] -= A[l]>>i & 1
                assert B[i] >= 0
            l += 1
            if all(B[i] <= 1 for i in range(M)):
                break
    assert r == N
    while l < r:
        if all(B[i] <= 1 for i in range(M)):
            ans += r - l
            break
        for i in range(M):
            B[i] -= A[l]>>i & 1
            assert B[i] >= 0
        l += 1

    print(ans)


def solve_ref(N: int, A: "List[int]"):
    """https://atcoder.jp/contests/abc098/submissions/33941528"""
    r = 0
    cnt = [0 for _ in range(20)]
    ans = 0
    for l in range(N):
        while r < N and max(cnt) <= 1:
            a = bin(A[r])[2:][::-1]
            for i in range(len(a)):
                if a[i] == '1':
                    cnt[i] += 1
            r += 1

        if max(cnt) >= 2:
            r -= 1
            a = bin(A[r])[2:][::-1]
            for i in range(len(a)):
                if a[i] == '1':
                    cnt[i] -= 1

        ans += r - l

        a = bin(A[l])[2:][::-1]
        for i in range(len(a)):
            if a[i] == '1':
                cnt[i] -= 1
    print(ans)


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    solve_ref(N, A)


if __name__ == "__main__":
    main()
