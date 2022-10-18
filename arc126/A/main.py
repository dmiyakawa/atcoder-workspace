#!/usr/bin/env python3


def main():
    T = int(input())
    for _ in range(T):
        N2, N3, N4 = map(int, input().split())
        if N3//2 > N4:
            b = N4 + min(N2 // 2, N3//2 - N4)
            N2 -= (b - N4) * 2
            assert N2 >= 0
            ans = b + N2 // 5
        else:
            a = N3//2
            N4 -= N3//2
            c = min(N4//2, N2)
            N4 -= c * 2
            N2 -= c
            assert N4 >= 0
            assert N2 >= 0
            d = min(N4, N2 // 3)
            N2 -= d * 3
            # print("--", N2)
            ans = a + c + d + N2 // 5
            # print("#2", a, c, d, N2//5)
        print(ans)


if __name__ == "__main__":
    main()
