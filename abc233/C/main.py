#!/usr/bin/env python3


def main():
    N, X = map(int, input().split())
    L = []
    for _ in range(N):
        lst = [int(e) for e in input().split()]
        L.append(lst[1:])
    d = {X: 1}
    for l in L:
        next_d = {}
        for a in l:
            for x, num in d.items():
                if x % a == 0:
                    next_d[x // a] = next_d.get(x // a, 0) + num
        d = next_d
    print(d.get(1, 0))


if __name__ == "__main__":
    main()
