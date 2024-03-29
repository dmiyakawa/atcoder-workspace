#!/usr/bin/env python3

def solve(K: int, S: int):
    count = 0
    for x in range(K + 1):
        for y in range(K + 1):
            if 0 <= S - x - y <= K:
                count += 1
    print(count)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(K, S)


if __name__ == "__main__":
    main()
