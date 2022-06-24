#!/usr/bin/env python3


def main():
    T = int(input())
    for _ in range(T):
        R, G, B = sorted(int(e) for e in input().split())
        if R == G or G == B:
            print(G)
            continue
        # R < G < B として
        # (R, G, B) -> (0, G-R, B-R) (操作回数R回に相当)
        count, R, G, B = R, 0, G - R, B - R
        if B == G:
            print(count + B)
            continue
        if G % 3 == 0:
            # G = 3*g として (0, 3*g, B) -> (2*g, 2*g, B - g) -> (0, 0, B - 3g) (完成)
            print(count + G)
            continue
        # B を G <= B の範囲で最小にする
        # (0, G, B) -> (2, G - 1, B - 1) -> (1, G + 1, B - 2) -> (0, G, B - 3)
        # (操作回数3回に相当。これを (B - R) // 3 回繰り返す)
        count += ((B - G) // 3) * 3
        B = B - ((B - G) // 3) * 3
        # (0, G, G + 1) or (0, G, G + 2)
        # print(f"({R}, {G}, {B}) ({count})")
        if B == G:
            print(count + B)
            continue
        if G % 3 == 1:
            if G + 1 == B:
                # (0, 3*g + 1, 3*g + 2) -> (0, 1, 2) (目標達成不可能)
                print(-1)
            else:
                # (0, 3*g + 1, 3*g + 2) -> (0, 1, 3) -> (2, 0, 2) -> (0, 0, 4) (完成)
                print(count + (G // 3) * 3 + 3)
        else:  # G % 3 == 2
            if G + 1 == B:
                # (0, 3*g + 2, 3*g + 3) -> (0, 2, 3) -> (2, 1, 2) -> (0, 5, 0) (完成)
                print(count + (G // 3) * 3 + 3)
            else:
                # (0, 3*g + 2, 3*g + 4) -> (0, 2, 4) -> (2, 1, 3) -> (0, 1, 2) (目標達成不可能)
                print(-1)


if __name__ == "__main__":
    main()
