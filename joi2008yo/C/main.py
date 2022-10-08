#!/usr/bin/env python3
from bisect import bisect

def solve(N, taro):
    all_cards = set(n for n in range(1, 2 * N + 1))
    taro = sorted(taro)
    hanako = sorted(all_cards - set(taro))
    turn = 0
    cur = 0
    while taro and hanako:
        # print(taro, hanako)
        p = hanako if turn else taro
        i = bisect(p, cur)
        if i < len(p):
            # print("hanako" if turn else "taro", cur, p[i])
            cur = p[i]
            del p[i]
        else:
            # print("hanako" if turn else "taro", cur, "skip")
            cur = 0
        turn = (turn + 1) % 2
    print(len(hanako))
    print(len(taro))


def main():
    N = int(input())
    taro = [int(input()) for _ in range(N)]
    solve(N, taro)


def _debug():
    from random import sample
    N = 100
    taro = sample(range(1, 2 * N + 1), N)
    solve(N, taro)


if __name__ == "__main__":
    # _debug()
    main()
