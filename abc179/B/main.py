#!/usr/bin/env python3

import sys

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(2)] for _ in range(N)]  # type: "List[List[int]]"
    print("Yes" if solve(N, D) else "No")


def solve(N: int, D: "List[List[int]]"):
    count = 0
    for t in (e[0] == e[1] for e in D):
        if t:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False


if __name__ == "__main__":
    main()
