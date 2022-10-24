#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, x: int, y: int, A: "List[int]"):
    possibles_1 = {A[0]}
    hor_max = sum(A[i] for i in range(N) if i % 2 == 0) - A[0]
    for i in range(2, N, 2):
        hor_max -= A[i]
        next_possibles = set()
        for px in possibles_1:
            for a in [A[i], -A[i]]:
                if abs(px + a - x) <= hor_max:
                    next_possibles.add(px + a)
        possibles_1 = next_possibles
    if x not in possibles_1:
        print(NO)
        return

    possibles_2 = {0}
    ver_max = sum(A[i] for i in range(N) if i % 2 == 1)
    for i in range(1, N, 2):
        ver_max -= A[i]
        next_possibles = set()
        for py in possibles_2:
            for b in [A[i], -A[i]]:
                if abs(py + b - y) <= ver_max:
                    next_possibles.add(py + b)
        possibles_2 = next_possibles

    if y not in possibles_2:
        print(NO)
        return
    print(YES)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, x, y, A)


if __name__ == "__main__":
    main()
