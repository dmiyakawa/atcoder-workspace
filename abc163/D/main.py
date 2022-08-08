#!/usr/bin/env python3


MOD = 1000000007  # type: int



def main():
    N, K = map(int, input().split())
    solve(N, K)


def solve(N: int, K: int):
    s1 = sum(range(K)) % MOD
    s2 = sum(range(N, N - K, -1)) % MOD
    ans = s2 - s1 + 1
    for i in range(K, N + 1):
        s1 += i
        s2 += N - i
        ans = (ans + s2 - s1 + 1) % MOD
    print(ans % MOD)




if __name__ == "__main__":
    main()
