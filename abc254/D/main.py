#!/usr/bin/env python3
#
# https://atcoder.jp/contests/abc254/editorial/4069
# https://twitter.com/kyopro_friends/status/1533082728446320640
#

def main():
    N = int(input())
    ans = 0
    for n in range(1, N+1):
        k = n
        d = 2
        while d * d <= k:
            while k % (d * d) == 0:
                k //= d * d
            d += 1
        d = 1
        count = 0
        while True:
            if k * d * d > N:
                break
            count += 1
            d += 1
        ans += count
    print(ans)


if __name__ == "__main__":
    main()
