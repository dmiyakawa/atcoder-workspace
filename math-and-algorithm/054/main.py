#!/usr/bin/env python3

import math


class Mat:
    def __init__(self, N, mod):
        self._mul = [((1, 1), (1, 0))]
        self._mod = mod
        i = 1
        while i <= int(math.log2(N)):
            self._mul.append(self.__class__.mul_with_mod(self._mul[i - 1], self._mul[i - 1], mod=self._mod))
            i += 1

    @staticmethod
    def mul_with_mod(a, b, mod):
        ret = []
        for i, row in enumerate(a):
            ret.append(tuple(sum(row[l] * b[l][j] % mod for l in range(len(a))) % mod for j in range(len(b[0]))))
        return tuple(ret)

    def fib(self, n):
        if n <= 2:
            return 1
        m = n
        grid = ((1, 0), (0, 1))
        i = 0
        while m:
            if m & 1:
                grid = self.mul_with_mod(self._mul[i], grid, self._mod)
            i += 1
            m >>= 1
        return grid[1][0]


def main():
    N = int(input())
    mat = Mat(N, 10**9)
    print(mat.fib(N))


if __name__ == "__main__":
    main()
