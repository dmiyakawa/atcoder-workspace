#!/usr/bin/env python3

MIN_N = 1
MAX_N = 10 ** 9


def main():
    A, B, X = [int(e) for e in input().split()]
    print(solve(A, B, X))


def calc_price(A, B, n):
    d = len(str(n))
    return A * n + B * d


def solve_slow(A, B, X):
    answer = 0
    for n in range(MIN_N, MAX_N + 1):
        price = calc_price(A, B, n)
        if price <= X:
            answer = n
            if price == X:
                break
        else:
            break
    return answer


def solve(A, B, X):
    left, right = MIN_N, MAX_N
    answer = 0
    while left <= right:
        n = (left + right) // 2
        price = calc_price(A, B, n)
        if X == price:
            answer = n
            break
        elif X < price:
            right = n - 1
        elif price < X:
            answer = n
            left = n + 1
    return answer


if __name__ == "__main__":
    main()
