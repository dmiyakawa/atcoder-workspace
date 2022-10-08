#!/usr/bin/env python3

from collections import deque, Counter


def solve(S: str):
    deq = deque(S)
    c = Counter(S)

    ans = 0
    while c["W"] > 0 and c["B"] > 0:
        ans += 1
        p = deq.pop()
        c[p] -= 1
        while p == deq[-1]:
            deq.pop()
            c[p] -= 1
    print(ans)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
