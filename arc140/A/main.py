#!/usr/bin/env python3
from collections import Counter


def main():
    N, K = [int(e) for e in input().split()]
    S = input()
    ans = N
    for n in range(1, N):
        if N % n != 0:
            continue
        count = K
        for i in range(n):
            counter = Counter(S[n * m + i] for m in range(N // n))
            count -= sum([tup[1] for tup in counter.most_common()[1:]])
            if count < 0:
                break
        if count >= 0:
            ans = n
            break

    print(ans)


if __name__ == "__main__":
    main()
