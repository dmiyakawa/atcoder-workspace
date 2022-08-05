#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    lamps = {}
    for i in range(M):
        lamps[i] = [int(e) - 1 for j, e in enumerate(input().split()) if j > 0]
    P = [int(e) for e in input().split()]
    count = 0
    for n in range(2**N):
        if all(sum(n >> j & 1 for j in lamps[i]) % 2 == P[i] for i in range(M)):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
