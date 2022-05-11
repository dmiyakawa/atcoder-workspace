#!/usr/bin/env python3

def prime_check_by_miller_rabin(n: int):

    def _suspect(a, t, _n):
        x = pow(a, t, _n)
        n1 = _n - 1
        while t != n1 and x != 1 and x != n1:
            x = pow(x, 2, _n)
            t <<= 1
        return t & 1 or x == n1

    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    check_list = (2, 7, 61) if n < 2 ** 32 else (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for i in check_list:
        if i >= n:
            break
        if not _suspect(i, d, n):
            return False
    return True


def main():
    N = int(input())
    primes = []
    count = 0
    for q in range(10**6 + 1):
        q3 = q ** 3
        if q3 >= N:
            break
        if not prime_check_by_miller_rabin(q):
            continue
        for prime in primes:
            if prime * q3 > N:
                break
            count += 1
        primes.append(q)
    print(count)


if __name__ == "__main__":
    main()
