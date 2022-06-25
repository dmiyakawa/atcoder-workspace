#!/usr/bin/env python3

import sys

sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: "List[int]"):
    num_0 = [0 for _ in range(31)]
    num_1 = [0 for _ in range(31)]
    for a in A:
        i = 0
        while i <= 30:
            if a & 2**i:
                num_1[i] += 1
            else:
                num_0[i] += 1
            i += 1
    # print(num_0, num_1)
    for i in range(31):
        if not (num_1[i] == 0 or (num_0[i] > 0 and num_0[i] * 2 == num_1[i])):
            return False
    As = set(A)
    if len(As) == 1:
        return True
    elif len(As) == 2:
        a = As.pop()
        b = As.pop()
        ac = A.count(a)
        bc = A.count(b)
        return ac == bc * 2 or ac * 2 == bc
    elif len(As) == 3:
        a, b, c = As.pop(), As.pop(), As.pop()
        ac, bc, cc = A.count(a), A.count(b), A.count(c)
        return ac == bc == cc


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(YES if solve(N, a) else NO)


if __name__ == "__main__":
    main()
