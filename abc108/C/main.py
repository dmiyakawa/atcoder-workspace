#!/usr/bin/env python3


def solve(N: int, K: int):
    mod_d = {}
    for a in range(1, N + 1):
        m = a % K
        mod_d[m] = mod_d.get(m, 0) + 1

    ans = 0

    if mod_d.get(0):
        ans += mod_d[0]**3
    if K % 2 == 0 and mod_d.get(K // 2):
        ans += mod_d[K // 2]**3
    print(ans)


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


if __name__ == "__main__":
    main()
