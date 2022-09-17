#!/usr/bin/env python3


def solve(Q: int, L: "List[int]", R: "List[int]"):
    primes = list_primes(10**5)
    primes_set = set(primes)
    lst = [p for p in primes if (p + 1) // 2 in primes_set]
    nums = [0] * (10**5 + 1)
    j = 0
    c = 0
    for i in range(10**5 + 1):
        if j < len(lst) and i == lst[j]:
            c += 1
            j += 1
        nums[i] = c

    for l, r in zip(L, R):
        print(nums[r] - nums[l - 1])


def list_primes(n):
    """nまでの素数をエラトステネスの篩を用いて求める（nを含む）"""
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

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(Q, l, r)


if __name__ == "__main__":
    main()
