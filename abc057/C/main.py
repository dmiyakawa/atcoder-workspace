#!/usr/bin/env python3


def main():
    N = int(input())
    print(min(max(len(str(N // n)), len(str(n))) for n in make_divisors(N)))


def make_divisors(n):
    """nの約数を列挙する"""
    # https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


if __name__ == "__main__":
    main()
