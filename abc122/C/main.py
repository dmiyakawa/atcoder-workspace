#!/usr/bin/env python3




def solve(N: int, Q: int, S: str, l: "List[int]", r: "List[int]"):
    B = [0] * N
    state = 0
    for i, ch in enumerate(S):
        B[i] = B[i - 1] if i > 0 else 0
        if ch == "A":
            state = 1
        else:
            if state == 1 and ch == "C":
                B[i] += 1
            state = 0
    for l0, r0 in zip(l, r):
        l0 -= 1
        r0 -= 1
        print(B[r0] - B[l0])


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, S, l, r)


if __name__ == "__main__":
    main()
