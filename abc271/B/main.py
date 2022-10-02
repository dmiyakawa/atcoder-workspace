#!/usr/bin/env python3



def main():
    N, Q = map(int, input().split())
    lst = []
    for _ in range(N):
        x = input().split()
        lst.append(x[1:])
    for _ in range(Q):
        s, t = map(int, input().split())
        print(lst[s - 1][t - 1])


if __name__ == "__main__":
    main()
