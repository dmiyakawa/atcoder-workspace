#!/usr/bin/env python3


def main():
    N, Q = map(int, input().split())
    lst = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(Q):
        query = [int(e) for e in input().split()]
        t = query[0]
        a = query[1] - 1
        if t == 1:
            b = query[2] - 1
            lst[a][b] = 1
        elif t == 2:
            to_follow = set(i for i in range(N) if lst[i][a] == 1)
            for i in range(N):
                if i in to_follow:
                    lst[a][i] = 1
        else:
            s = set(i for i in range(N) if lst[a][i] == 1)
            to_follow = set()
            for f_id in s:
                to_follow |= set(i for i in range(N) if lst[f_id][i] == 1)

            to_follow.discard(a)
            for i in range(N):
                if i in to_follow:
                    lst[a][i] = 1
    for row in lst:
        print("".join("Y" if i == 1 else "N" for i in row))


if __name__ == "__main__":
    main()
