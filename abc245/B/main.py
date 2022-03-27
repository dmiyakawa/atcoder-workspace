#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


def solve(N: int, A: "List[int]"):
    appeared = set()
    current_min = 0
    for a in A:
        appeared.add(a)
        while current_min in appeared:
            current_min += 1
    print(current_min)


if __name__ == "__main__":
    main()
