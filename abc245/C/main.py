#!/usr/bin/env python3


YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A, B)


def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    possibles = [{A[0], B[0]}]
    is_possible = True
    for i in range(1, N):
        a, b = A[i], B[i]
        next_possibles = set()
        for x in possibles[i - 1]:
            if abs(x - a) <= K:
                next_possibles.add(a)
            if abs(x - b) <= K:
                next_possibles.add(b)
        if not next_possibles:
            is_possible = False
            break
        possibles.append(next_possibles)
    print(YES if is_possible else NO)


if __name__ == "__main__":
    main()
