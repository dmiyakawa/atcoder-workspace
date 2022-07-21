#!/usr/bin/env python3

def main():
    # 提出時解法
    N = int(input())
    H = [int(e) for e in input().split()]
    max_H = max(H)
    count = 0
    for h in range(max_H, 0, -1):
        left = None
        for i, h0 in enumerate(H):
            if h0 >= h:
                if left is None:
                    left = i
            elif left is not None:
                count += 1
                left = None
        if left is not None:
            count += 1
    print(count)


def main_ref():
    # 解説の解法 https://atcoder.jp/contests/abc116/editorial/3024
    N = int(input())
    H = [0] + [int(e) for e in input().split()] + [0]
    print(sum(abs(H[i + 1] - H[i]) for i in range(N + 1)) // 2)


if __name__ == "__main__":
    main_ref()
