#!/usr/bin/env python3

def solve(N: int) -> int:
    # pow() を素直に使うと誤差でWAを食らう
    # 5489031744 ** (1/3) = 1763.9999999999993 となって誤差で落ちる
    # import math
    # p3 = math.floor(N ** (1/3))
    # p2 = math.floor(N ** (1/2))
    count = 0
    for a in range(1, N + 1):
        if a * a * a > N:
            break
        for b in range(a, N + 1):
            if a * b * b > N:
                break
            count += N // (a * b) - b + 1

    print(count)


def main():
    solve(int(input()))


if __name__ == "__main__":
    main()
