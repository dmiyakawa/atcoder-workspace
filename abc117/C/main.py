#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    X = sorted(int(e) for e in input().split())
    if N >= M:
        print(0)
        return
    links = []
    for i in range(M - 1):
        links.append((X[i + 1] - X[i], i))
    links.sort(reverse=True)
    print(sum(d for d, _ in links[(N-1):]))


if __name__ == "__main__":
    main()
