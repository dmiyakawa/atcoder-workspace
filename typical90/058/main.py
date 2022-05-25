#!/usr/bin/env python3


MOD = 10  # type: int


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


def solve(N: int, K: int):
    cache = {}
    count = 1
    cur_value = N
    prev_value = None
    if N == 0:
        print(0)
        return

    while cur_value not in cache:
        next_value = (cur_value + sum(int(e) for e in str(cur_value))) % 10**5
        cache[cur_value] = (next_value, count)
        prev_value = cur_value
        cur_value = next_value
        count += 1
    cycle_start = cache[cur_value][1]
    cycle_end = cache[prev_value][1]
    cycle = (cycle_end - cycle_start) + 1

    cur_value = N
    if K < cycle_end:
        for count in range(K):
            cur_value = cache[cur_value][0]
    else:
        for count in range(cycle_start):
            cur_value = cache[cur_value][0]
        for count in range((K - cycle_start) % cycle):
            cur_value = cache[cur_value][0]

    print(cur_value)


if __name__ == "__main__":
    main()
