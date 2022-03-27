#!/usr/bin/env python3

import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List, Optional

T = TypeVar("T")


class SortedMultiset(Generic[T]):
    """\
    平方分割を利用したSortedMultiSet
    ref. https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
    """

    BUCKET_RATIO = 500
    REBUILD_RATIO = 1000

    def _build(self, a: Optional[Iterable[T]] = None) -> None:
        """Evenly divide `a` into buckets."""
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size:size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a: Optional[Iterable[T]] = None) -> None:
        """Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"""
        self.a = None
        self.size = None
        a = list(a) if a is not None else []
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1:len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        """Find the bucket which should contain x. self must not be empty."""
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        """Count the number of x."""
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        """Add an element. / O(√N)"""
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def remove(self, x: T):
        if not self.discard(x):
            raise ValueError(f"{x} not found")

    def discard(self, x: T) -> bool:
        """Remove an element and return True if removed. / O(√N)"""
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x:
            return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0:
            self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        """Find the largest element < x, or None if it doesn't exist."""
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
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for a in self.a:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        """Count the number of elements < x."""
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


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    D = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A, B, C, D)


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    lst = [(h, w, "c") for h, w in zip(A, B)] + [(h, w, "b") for h, w in zip(C, D)]
    lst.sort(key=lambda tup: (-tup[0], tup[2]))

    possible = True
    ms = SortedMultiset()
    for i, (h, w, t) in enumerate(lst):
        if t == "b":
            ms.add(w)
        else:
            ge = ms.ge(w)
            if ge is None:
                possible = False
            else:
                ms.remove(ge)

    print(YES if possible else NO)


if __name__ == "__main__":
    main()
