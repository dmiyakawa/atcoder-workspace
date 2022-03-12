#!/usr/bin/env python3


def main():
    import sys

    N, X = [int(e) for e in sys.stdin.readline().split()]
    S = sys.stdin.readline().rstrip()

    # 10 ** 18 -> 18 chars
    X_lst = [int(ch) for ch in "{:b}".format(X)]
    for s in S:  # 10 ** 6
        if s == "U":
            X_lst.pop()
        elif s == "R":
            X_lst.append(1)
        else:
            X_lst.append(0)
    answer = 0
    for i, digit in enumerate(reversed(X_lst)):
        if digit == 1:
            answer += int(digit) * (2 ** i)
    print(answer, end="")


if __name__ == "__main__":
    main()
