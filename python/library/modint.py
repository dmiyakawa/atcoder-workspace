#
# - _math.py への依存を削除
# - 静的メソッド ModInt.raw() の追加
#

import typing


class ModContext:
    context: typing.List[int] = []

    def __init__(self, mod: int) -> None:
        assert 1 <= mod

        self.mod = mod

    def __enter__(self) -> None:
        self.context.append(self.mod)

    def __exit__(
        self, exc_type: typing.Any, exc_value: typing.Any, traceback: typing.Any
    ) -> None:
        self.context.pop()

    @classmethod
    def get_mod(cls) -> int:
        return cls.context[-1]


class Modint:
    def __init__(self, v: int = 0) -> None:
        self._mod = ModContext.get_mod()
        if v == 0:
            self._v = 0
        else:
            self._v = v % self._mod

    def mod(self) -> int:
        return self._mod

    def val(self) -> int:
        return self._v

    @staticmethod
    def raw(v: int) -> "Modint":
        x = Modint()
        x._v = v
        return x

    @staticmethod
    def _inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
        a %= b
        if a == 0:
            return b, 0

        # Contracts:
        # [1] s - m0 * a = 0 (mod b)
        # [2] t - m1 * a = 0 (mod b)
        # [3] s * |m1| + t * |m0| <= b
        s = b
        t = a
        m0 = 0
        m1 = 1

        while t:
            u = s // t
            s -= t * u
            m0 -= m1 * u  # |m1 * u| <= |m1| * s <= b

            # [3]:
            # (s - t * u) * |m1| + t * |m0 - m1 * u|
            # <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)
            # = s * |m1| + t * |m0| <= b

            s, t = t, s
            m0, m1 = m1, m0

        # by [3]: |m0| <= b/g
        # by g != b: |m0| < b/g
        if m0 < 0:
            m0 += b // s

        return s, m0

    def __iadd__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            self._v += rhs._v
        else:
            self._v += rhs
        if self._v >= self._mod:
            self._v -= self._mod
        return self

    def __isub__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            self._v -= rhs._v
        else:
            self._v -= rhs
        if self._v < 0:
            self._v += self._mod
        return self

    def __imul__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            self._v = self._v * rhs._v % self._mod
        else:
            self._v = self._v * rhs % self._mod
        return self

    def __ifloordiv__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = self.__class__._inv_gcd(rhs, self._mod)[1]
        self._v = self._v * inv % self._mod
        return self

    def __pos__(self) -> "Modint":
        return self

    def __neg__(self) -> "Modint":
        return Modint() - self

    def __pow__(self, n: int) -> "Modint":
        assert 0 <= n

        return Modint(pow(self._v, n, self._mod))

    def inv(self) -> "Modint":
        eg = self.__class__._inv_gcd(self._v, self._mod)

        assert eg[0] == 1

        return Modint(eg[1])

    def __add__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            result = self._v + rhs._v
            if result >= self._mod:
                result -= self._mod
            return self.__class__.raw(result)
        else:
            return Modint(self._v + rhs)

    def __sub__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            result = self._v - rhs._v
            if result < 0:
                result += self._mod
            return self.__class__.raw(result)
        else:
            return Modint(self._v - rhs)

    def __mul__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            return Modint(self._v * rhs._v)
        else:
            return Modint(self._v * rhs)

    def __floordiv__(self, rhs: typing.Union["Modint", int]) -> "Modint":
        if isinstance(rhs, Modint):
            inv = rhs.inv()._v
        else:
            inv = self.__class__._inv_gcd(rhs, self._mod)[1]
        return Modint(self._v * inv)

    def __eq__(self, rhs: typing.Union["Modint", int]) -> bool:  # type: ignore
        if isinstance(rhs, Modint):
            return self._v == rhs._v
        else:
            return self._v == rhs

    def __ne__(self, rhs: typing.Union["Modint", int]) -> bool:  # type: ignore
        if isinstance(rhs, Modint):
            return self._v != rhs._v
        else:
            return self._v != rhs

