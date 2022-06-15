#!/usr/bin/env python3

def main():
    N = int(input())
    P = []
    for _ in range(N):
        P.append(int(input()))

    seqs = {}
    max_len = 0
    for p in P:
        if p - 1 in seqs:
            seqs[p - 1].append(p)
            seqs[p] = seqs[p - 1]
        else:
            seqs[p] = [p]
        max_len = max(max_len, len(seqs[p]))
    print(N - max_len)


if __name__ == "__main__":
    main()
