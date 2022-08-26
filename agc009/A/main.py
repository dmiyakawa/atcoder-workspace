#!/usr/bin/env python3



def solve(N: int, A: "List[int]", B: "List[int]"):
    count = 0
    for a, b in zip(reversed(A), reversed(B)):
        cur = a + count
        if cur % b == 0:
            pass
        elif cur <= b:
            count += b - cur
        else:
            num = cur // b + (1 if cur % b else 0)
            count += b * num - cur
    print(count)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == "__main__":
    main()
