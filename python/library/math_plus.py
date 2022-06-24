#!/usr/bin/env python3

import functools
import math
import unittest
from typing import Dict


def gcd_all(*args):
    """多引数版のgcd(最大公約数を求める)。Python 3.9 以降では標準ライブラリにはある"""
    ret = None
    for arg in args:
        if ret is None:
            ret = arg
            continue
        ret = math.gcd(ret, arg)
    return ret


def lcm(a, b):
    """aとbの最小公倍数を求める"""
    return a // math.gcd(a, b) * b


def lcm_all(*args):
    """多引数版のlcm"""
    return functools.reduce(lcm, args)


# https://qiita.com/derodero24/items/91b6468e66923a87f39f
# Python 3.8 では math.comb() の代替
# Nが巨大でmod pが想定される場合にはModCombを使うこと
def comb(n, r):
    """nCr を計算する。 factorial(N) // factorial(N - r) // factorial(r) より概して高速"""
    from operator import mul
    from functools import reduce
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


# See also https://twitter.com/kyopro_friends/status/1502672419299164160
# > sqrtで誤差が出るのは引数がdoubleにキャストされるせいです
# > なので、doubleで正確に表すことのできない10^16前後から誤差が出ます
def sqrt_int(x) -> int:
    xx = int(math.sqrt(x) // 1)
    ans = 0
    for i in range(-1, 2):
        tmp = xx + i
        if tmp >= 0:
            if tmp * tmp <= x:
                ans = tmp
    return ans


def _sqrt_check():
    # sqrt()がズレる実例が分からない
    import random
    while True:
        val = random.randrange(10 ** 16, 10 ** 16 + 10 ** 8)
        a = sqrt_int(val)
        b = int(math.sqrt(val))
        if a != b:
            print(val, a, b)
            break


def pow_int_with_mod(x: int, y: int, m: int) -> int:
    """\
    x^y mod m を返す。x, y, mはすべて正の整数とする
    x, y は10^9など非常に大きい際にもmを用いてそこそこ高速に動作することを目標とする
    """
    # TODO: 繰り返し2乗法ｘｓ
    assert x > 0 and isinstance(x, int)
    assert y > 0 and isinstance(y, int)
    assert m > 0 and isinstance(m, int)
    if x < 1000 or y < 1000:
        return int(x ** y % m)
    y_rem = y
    to_be_multiplied = x % m
    ans = 1
    while y_rem:
        to_multiply = to_be_multiplied ** (y_rem % 10) % m
        ans = (ans * to_multiply) % m
        to_be_multiplied = (to_be_multiplied ** 10) % m
        y_rem //= 10
    return ans


class PowIntWithModTest(unittest.TestCase):
    def test_pow_int_with_mod(self):
        self.assertEqual(pow_int_with_mod(10, 10, 3), 1)
        self.assertEqual(pow_int_with_mod(9999, 10000, 1000000007), 616673012)
        self.assertEqual(pow_int_with_mod(9999, 100000, 1000000007), 207398859)


def factorize_in_prime(n) -> "Dict[int, int]":
    """2以上の整数nを素因数分解し、{素因数: 指数, ...}の辞書を返す"""
    # https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
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


class FactorizeInPrimeTest(unittest.TestCase):
    def test_factorize_in_prime(self):
        self.assertEqual(factorize_in_prime(12), {2: 2, 3: 1})
        self.assertEqual(factorize_in_prime(7), {7: 1})
        self.assertEqual(factorize_in_prime(1014), {2: 1, 3: 1, 13: 2})


# https://ikatakos.com/pot/programming_algorithm/number_theory/prime_judge
# 2^64までの決定的アルゴリズムとして実装しているので、ランダム要素は無い
def prime_check_by_miller_rabin(n: int):
    """ミラーラビン素数判定法を用いて与えられた正の整数が素数であるかを返す"""

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


class PrimeCheckTest(unittest.TestCase):
    def test_prime_check_by_miller_rabin(self):
        self.assertFalse(prime_check_by_miller_rabin(1))
        self.assertTrue(prime_check_by_miller_rabin(2))
        self.assertTrue(prime_check_by_miller_rabin(3))
        self.assertTrue(prime_check_by_miller_rabin(8_191))
        self.assertTrue(prime_check_by_miller_rabin(33_333_331))
        self.assertFalse(prime_check_by_miller_rabin(333_333_331))
        self.assertTrue(prime_check_by_miller_rabin(67_280_421_310_721))


def modinv(a: int, mod: int):
    """非再帰拡張 Euclid の互除法によるmod逆元。modは素数である必要はない"""
    b, u, v = mod, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u


def modpow(a: int, n: int, mod: int):
    """a^n mod mod を計算する"""
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


class ModInvTest(unittest.TestCase):
    def test_modinv(self):
        self.assertEqual(499122177, modinv(2, 998244353))
        self.assertEqual(500000004, modinv(2, 1000000007))


if __name__ == "__main__":
    _sqrt_check()

