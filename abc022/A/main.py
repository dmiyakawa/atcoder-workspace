#!/usr/bin/env python3

def main():
    N, S, T = [int(e) for e in input().split()]
    W = int(input())
    As = [0] + [int(input()) for _ in range(N-1)]
    count = 0
    for a in As:
        W += a
        if S <= W <= T:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
