#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    dp = {(0, N - 1): 0}
    t = True

    for n in range(1, N + 1):
        new_dp = {}
        # n手終了時に左からl_n個、右からr_n個取り除いた場合
        for l_n in range(n + 1):
            r_n = n - l_n
            l = l_n
            r = N - 1 - r_n
            if t:
                if l_n > 0:
                    v = dp[(l - 1, r)] + A[l - 1]
                    new_dp[(l, r)] = max(dp[(l, r)], v) if (l, r) in dp else v
                if r_n > 0:
                    v = dp[(l, r + 1)] + A[r + 1]
                    new_dp[(l, r)] = max(dp[(l, r)], v) if (l, r) in dp else v
            else:
                if l_n > 0:
                    v = dp[(l - 1, r)] - A[l - 1]
                    new_dp[(l, r)] = min(dp[(l, r)], v) if (l, r) in dp else v
                if r_n > 0:
                    v = dp[(l, r + 1)] - A[r + 1]
                    new_dp[(l, r)] = min(dp[(l, r)], v) if (l, r) in dp else v
            print(n, l_n, r_n, " ", l, r, new_dp[(l, r)])
        print(new_dp)
        dp = new_dp
        t = not t
    print(dp)
    print(max(dp.values()) if t else min(dp.values()))


if __name__ == "__main__":
    main()
