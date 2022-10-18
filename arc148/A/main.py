#!/usr/bin/env python3


def solve(N: int, A: "List[int]"):
    import math
    M = math.ceil(math.sqrt(max(A)))
    print(M)
    primes = list_primes(M)
    ans = max(primes)
    for p in primes:
        ans = min(ans, len(set(a % p for a in A)))
    print(ans)


def list_primes(n):
    ret = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(n + 1):
        if not is_prime[i]:
            continue
        ret.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

    return ret


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
