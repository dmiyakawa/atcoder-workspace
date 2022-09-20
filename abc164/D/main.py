#!/usr/bin/env python3


def solve(S: str):
    count = 0
    prev_ms = [0] * 2019
    for i in range(len(S) - 3):
        v = int(S[i:i + 4])
        v0 = int(S[i + 3])
        # print(i, prev_ms, count, v)
        m = v % 2019
        if m == 0:
            count += 1
        next_ms = [0] * 2019
        next_ms[m] = 1
        for prev_m, num in enumerate(prev_ms):
            m = (prev_m * 10 + v0) % 2019
            if m == 0:
                count += num
            next_ms[m] += num
        prev_ms = next_ms
    print(count)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    solve(next(tokens))


if __name__ == "__main__":
    main()
