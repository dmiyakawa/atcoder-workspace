#!/usr/bin/env python3
#
# https://atcoder.jp/contests/abc249/editorial/3786
# https://atcoder.jp/contests/abc249/submissions/31210498
#

def main():
    input()
    a = sorted(map(int, input().split()))
    d = {}
    for i in a:
        d[i] = d.get(i, 0) + 1
    a = set(a)
    val = max(a)
    count = 0
    for i in a:
        for j in a:
            count += d.get(i * j, 0) * d[i] * d[j]
            if i * j > val:
                break
    print(count)


if __name__ == "__main__":
    main()
