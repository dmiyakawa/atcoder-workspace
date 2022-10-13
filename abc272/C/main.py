#!/usr/bin/env python3



def solve(N: int, A: "List[int]"):
    B = sorted(a for a in A if a % 2 == 0)
    C = sorted(a for a in A if a % 2 != 0)
    b = sum(B[-2:]) if len(B) >= 2 else -1
    c = sum(C[-2:]) if len(C) >= 2 else -1
    print(max(b, c))


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
