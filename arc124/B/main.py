#!/usr/bin/env python3



def solve(N: int, A: "List[int]", B: "List[int]"):
    M = 0
    for a, b in zip(A, B):
        count = 0
        while a or b:
            a >>= 1
            b >>= 1
            count += 1
        M = max(M, count)
    da = {}
    for a in A:
        da0 = da
        for i in range(M - 1, 0, -1):
            da0 = da0.setdefault((a >> i) & 1, {})
        da0.setdefault(a & 1, set()).add(a)

    db = {}
    for b in B:
        db0 = db
        for i in range(M - 1, 0, -1):
            db0 = db0.setdefault((b >> i) & 1, {})
        db0.setdefault(b & 1, set()).add(b)

    def gen(_da, _db):
        if isinstance(_da, set) and isinstance(_db, set):
            ...


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, b)


if __name__ == "__main__":
    main()
