#!/usr/bin/env python3
from collections import defaultdict


def main():
    N, M = map(int, input().split())
    friends = defaultdict(set)
    secondhands = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].add(b)
        friends[b].add(a)

    for n in range(1, N + 1):
        for m in friends[n]:
            for l in friends[m]:
                if l != n and l not in friends[n]:
                    secondhands[n].add(l)
        print(len(secondhands[n]))


if __name__ == "__main__":
    main()
