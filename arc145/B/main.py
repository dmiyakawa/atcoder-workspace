#!/usr/bin/env python3

def main():
    N, A, B = map(int, input().split())
    if N < A:
        return 0
    if A <= B:
        return N - A + 1
    num_lost = A - 1
    X = (N - (A - 1)) // A
    Y = (N - (A - 1)) % A
    num_lost += X * (A - B)
    num_lost += max(Y - B, 0)
    return N - num_lost


if __name__ == "__main__":
    print(main())
