#!/usr/bin/env python3

import functools
import math
import unittest


def gcd_all(*args):
    """多引数版のgcd。Python 3.9 以降では標準ライブラリにはある"""
    ret = None
    for arg in args:
        if ret is None:
            ret = arg
            continue
        ret = math.gcd(ret, arg)
    return ret


def lcm(a, b):
    return a // math.gcd(a, b) * b


def lcm_all(*args):
    return functools.reduce(lcm, args)


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


def _main():
    # しかしズレる実例が分からない
    import random
    while True:
        val = random.randrange(10 ** 16, 10 ** 16 + 10 ** 8)
        a = sqrt_int(val)
        b = int(math.sqrt(val))
        if a != b:
            print(val, a, b)
            break


if __name__ == "__main__":
    _main()

