#!/usr/bin/env python3


def solve(X: int):
    lst = [int(e) for e in str(X)]
    if len(lst) == 1:
        return X

    for i0 in range(lst[0], 10):
        for i1 in range(10):
            grad = i1 - i0
            cand = [i0, i1] + [i1 + grad * n for n in range(1, len(lst) - 1)]
            if any(v < 0 or v > 9 for v in cand):
                continue
            v = sum(n * 10 ** i for i, n in enumerate(reversed(cand)))
            if v < X:
                continue
            return v


def main():
    print(solve(int(input())))


if __name__ == "__main__":
    main()
