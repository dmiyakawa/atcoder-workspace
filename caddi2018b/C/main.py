#!/usr/bin/env python3



def solve(N: int, P: int):
    if P == 1:
        print(P)
        return
    d = factorize_in_prime(P)
    ans = 1
    for val, num in d.items():
        ans *= val ** (num // N)
    print(ans)


def factorize_in_prime(n) -> "Dict[int, int]":
    assert n >= 2
    d = {}
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                count += 1
                temp //= i
            d[i] = count

    if temp != 1:
        d[temp] = 1

    if not d:
        d[n] = 1

    return d



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(N, P)


if __name__ == "__main__":
    main()
