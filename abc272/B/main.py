#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N, M = map(int, input().split())
    combs = {(i, j) for i in range(N) for j in range(i + 1, N)}
    for _ in range(M):
        lst = list(map(int, input().split()))
        k = lst[0]
        del lst[0]
        for i in range(k):
            for j in range(i + 1, k):
                combs.discard((lst[i] - 1, lst[j] - 1))
    # print(combs)
    print(NO if combs else YES)

if __name__ == "__main__":
    main()
