#!/usr/bin/env python3
# 解説読解済


def main_x():
    # https://atcoder.jp/contests/abc172/submissions/14745136
    # 高速ゼータ変換……らしいが、わからん
    # numbaでないからか、遅い
    import numpy as np

    def prime_table(N):
        is_prime = np.zeros(N, np.int64)
        is_prime[2:3] = 1
        is_prime[3::2] = 1
        for p in range(3, N, 2):
            if p * p >= N:
                break
            if is_prime[p]:
                is_prime[p * p::p + p] = 0
        return is_prime, np.where(is_prime)[0]

    def solve(N, primes):
        div = np.ones(N + 1, dtype=np.int64)
        for p in primes:
            for i in range(N // p + 1):
                div[p * i] += div[i]
        div *= np.arange(N + 1)
        return div.sum()

    N = int(input())
    is_prime, primes = prime_table(N + 1)
    print(solve(N, primes))


def main():
    N = int(input())
    ans = 0
    for j in range(1, N + 1):
        y = N // j
        ans += (1 + y) * y * j // 2
    print(ans)


if __name__ == "__main__":
    main()
