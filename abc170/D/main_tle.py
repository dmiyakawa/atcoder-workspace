#!/usr/bin/env python3

import math
import sys
from bisect import bisect_left
from bisect import bisect_right
from typing import Iterator, Union
from typing import List, TypeVar, Generic, Iterable


def solve(N: int, A: "List[int]"):
    Ac1 = A.count(1)
    if Ac1 > 0:
        if Ac1 == 1:
            print(1)
        else:
            print(0)
        return
    A.sort()
    Ass = SortedSet(A)
    All = SortedSet(range(2, 10**6 + 1))
    for n in range(2, 1001):
        if n not in Ass:
            continue
        to_remove = set()
        for v in All:
            if v != n and v % n == 0:
                to_remove.add(v)
        for v in to_remove:
            All.discard(v)
    ans = 0
    for a in Ass:
        if a in All and bisect_right(A, a) - bisect_left(A, a) == 1:
            ans += 1
    print(ans)


T = TypeVar("T")


class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        """Evenly divides `a` into buckets."""
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = tuple()) -> None:
        """\
        Makes a new SortedSet from iterable.
        O(N) if sorted and unique. O(N log N) otherwise.
        """
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        """\
        Finds the bucket which should contain x.
        self.a must not be empty.
        """
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        """\
        Adds an element and return True if added. / O(√N)
        """
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        """\
        Removes an element and return True if removed. / O(√N)
        """
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        """Find the largest element that is less than x, or None if it doesn't exist."""
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        """Find the largest element <= x, or None if it doesn't exist."""
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        """Find the smallest element > x, or None if it doesn't exist."""
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        """Find the smallest element >= x, or None if it doesn't exist."""
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        """Return the x-th element, or IndexError if it doesn't exist."""
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        """Count the number of elements that are less than x"""
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        """Count the number of elements <= x."""
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


def main():

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
