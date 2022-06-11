#!/usr/bin/env python3


def main():
    N, A, B = [int(e) for e in input().split()]
    P, Q, R, S = [int(e) for e in input().split()]
    left_1 = max(1 - A, 1 - B)
    right_1 = min(N - A, N - B)
    left_2 = max(1 - A, B - N)
    right_2 = min(N - A, B - 1)
    for i in range(P, Q + 1):
        lst = []
        for j in range(R, S + 1):
            if i - A - left_1 == j - B - left_1 or i - A - left_2 == B - j - left_2:
                lst.append("#")
            else:
                lst.append(".")
        print("".join(lst))


if __name__ == "__main__":
    main()
