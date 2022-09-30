#!/usr/bin/env python3



def solve(N: int, A: "List[int]"):
    min_A = min(A)
    abs_sum = sum(abs(a) for a in A)
    if min_A < 0:
        num_negs = sum(1 if a < 0 else 0 for a in A)
        if num_negs % 2:
            print(abs_sum - min(abs(a) for a in A) * 2)
            return
    print(abs_sum)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

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
