#!/usr/bin/env python3

def solve(A, B):
    if A < B:
        A, B = B, A
    while True:
        m = A % B
        if m == 0:
            break
        else:
            A, B = B, A % B
    return B


def main():
    A, B = map(int, input().split())
    print(solve(A, B))


if __name__ == "__main__":
    main()
