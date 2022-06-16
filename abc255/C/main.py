#!/usr/bin/env python3

def solve(X, A, D, N):
    left = min(A, A + D * (N - 1))
    right = max(A, A + D * (N - 1))
    if X <= left:
        return abs(left - X)
    elif right <= X:
        return abs(right - X)
    else:
        step = abs(D)
        rem = X - left
        return min(rem % step, step - rem % step)


def main():
    X, A, D, N = [int(e) for e in input().split()]
    print(solve(X, A, D, N))


if __name__ == "__main__":
    main()
