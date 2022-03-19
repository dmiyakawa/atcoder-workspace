#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    V = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, Q, A, L, R, V)


def solve(N: int, Q: int, A: "List[int]", L: "List[int]", R: "List[int]", V: "List[int]"):
    score = 0
    diffs = []
    for i in range(N - 1):
        diff = A[i] - A[i + 1]
        diffs.append(diff)
        score += abs(diff)
    # print("first_score:", score)
    for l, r, v in zip(L, R, V):
        l = l - 1
        r = r - 1
        # print(f"l: {l}, r: {r}")
        if l - 1 >= 0:
            before = diffs[l - 1]
            after = before - v
            score = score - abs(before) + abs(after)
            diffs[l - 1] = after
            # print(before, after, score)
        if r + 1 < N:
            before = diffs[r]
            after = before + v
            score = score - abs(before) + abs(after)
            diffs[r] = after
            # print(before, after, score)
        print(score)


if __name__ == "__main__":
    main()
