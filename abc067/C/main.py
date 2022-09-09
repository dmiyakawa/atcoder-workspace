#!/usr/bin/env python3



def solve(N: int, A: "List[int]"):
    x = A[0]
    y = sum(A) - A[0]
    ans = abs(x - y)
    for a in A[1:-1]:
        x += a
        y -= a
        ans = min(ans, abs(x - y))
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
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == "__main__":
    main()
