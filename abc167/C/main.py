#!/usr/bin/env python3

Inf = float("inf")

def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for _ in range(N):
        lst = [int(e) for e in input().split()]
        C.append(lst[0])
        A.append(lst[1:])

    min_cost = Inf

    for n in range(2**N):
        skills = [0 for _ in range(M)]
        cost = 0
        for i in range(N):
            if (1 << i) & n:
                skills = [skill + A[i][j] for j, skill in enumerate(skills)]
                cost += C[i]
        possible = min(skills) >= X
        if possible:
            min_cost = min(min_cost, cost)
    if min_cost == Inf:
        print(-1)
    else:
        print(min_cost)


if __name__ == "__main__":
    main()
