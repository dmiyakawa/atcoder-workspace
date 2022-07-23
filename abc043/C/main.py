#!/usr/bin/env python3

Inf = float("inf")

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    min_cost = Inf
    for cand in range(-100, 101):
        min_cost = min(min_cost, sum((cand - A[i]) ** 2 for i in range(N)))
    print(min_cost)


if __name__ == "__main__":
    main()
