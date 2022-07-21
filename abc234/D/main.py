#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    P = [int(e) for e in input().split()]
    val = N - K + 1
    lst = [val]
    rem = set(P)
    for i in range(N - K):
        to_remove = P[N - 1 - i]
        rem.remove(to_remove)
        if to_remove > val:
            val -= 1
            while val not in rem:
                val -= 1
        lst.append(val)
    for v in reversed(lst):
        print(v)


if __name__ == "__main__":
    main()
