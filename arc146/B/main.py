#!/usr/bin/env python3


def solve_wa(N: int, M: int, K: int, A: "List[int]"):
    lb = 0
    for a in A:
        for i in range(34, 0, -1):
            if (a >> (i - 1)) & 1:
                lb = max(lb, i)
                break
    while lb > 0:
        lst = []
        for a in A:
            lst.append(max(2 ** (lb - 1) - a, 0))
        lst.sort()
        if sum(lst[:K]) > M:
            for i in range(N):
                A[i] &= 2 ** (lb - 1) - 1
            lb -= 1
        else:
            break
    B = sorted(A, reverse=True)[:K]
    # print(lb, A, B)
    ans = 0
    for i in range(34, 0, -1):
        lst = []
        for b in B:
            bb = b & (2 ** i - 1)
            lst.append(max(2 ** (i - 1) - bb, 0))
        count = sum(lst)
        if M >= count:
            # print(f"i: {i}, lst: {lst}, c: {count}, M: {M} -> {M - count}, ans: {ans} -> {ans | 2 ** (i - 1)}")
            M -= count
            for j, c in enumerate(lst):
                B[j] += c
            # print([format(b, "b") for b in B])
            ans |= 2 ** (i - 1)
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve_wa(N, M, K, A)


if __name__ == "__main__":
    main()
