#!/usr/bin/env python3
#
# Bellman-Ford, O(|V||E|)
# https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
#

Inf = float("inf")

def main():
    N, M, r = [int(e) for e in input().split()]
    links = {}
    for _ in range(M):
        s, t, d = map(int, input().split())
        links[(s, t)] = d

    costs = [Inf for _ in range(N)]
    costs[r] = 0
    cycle_detected = False
    for i in range(N):
        updated = False
        for (s, t), d in links.items():
            if costs[t] > costs[s] + d:
                costs[t] = costs[s] + d
                updated = True
        if updated:
            if i == N - 1:
                cycle_detected = True
        else:
            break
    if cycle_detected:
        print("NEGATIVE CYCLE")
    else:
        for cost in costs:
            if cost == Inf:
                print("INF")
            else:
                print(cost)


if __name__ == "__main__":
    main()
