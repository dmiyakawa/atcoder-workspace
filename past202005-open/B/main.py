#!/usr/bin/env python3


def main():
    N, M, Q = [int(e) for e in input().split()]
    solved = {i: set() for i in range(1, M + 1)}
    for _ in range(Q):
        query = [int(e) for e in input().split()]
        if query[0] == 1:
            n = query[1]
            print(sum(N - len(solved[i]) for i in range(1, M + 1) if n in solved[i]))
        else:
            n, m = query[1], query[2]
            solved[m].add(n)


if __name__ == "__main__":
    main()
