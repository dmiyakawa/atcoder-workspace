#!/usr/bin/env python3
#
# https://atcoder.jp/contests/past202112-open/submissions/32304911
#


class Dijkstra:
    def __init__(self, N, E, inf=1 << 50):
        self.N = N
        self.E = E
        self.inf = inf

    def cost_from(self, s):
        import heapq

        C = [self.inf] * self.N
        C[s] = 0
        h = [(0, s)]
        visited = set()

        while len(h) > 0:
            _, v = heapq.heappop(h)
            if v in visited:
                continue
            visited.add(v)

            for cost, dest in self.E[v]:
                if C[dest] > C[v] + cost:
                    C[dest] = C[v] + cost
                    heapq.heappush(h, (C[dest], dest))
        return C


def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    X = [1, N]
    for a, b, _ in edges:
        X.append(a)
        X.append(b)
    X = sorted(set(X))
    idx = {}
    for i, x in enumerate(X):
        idx[x] = i

    E = [[] for _ in range(len(X))]
    for a, b, c in edges:
        ai, bi = idx[a], idx[b]
        E[ai].append((c, bi))
        E[bi].append((c, ai))
    for s, t in zip(X[:-1], X[1:]):
        si, ti = idx[s], idx[t]
        E[si].append((t - s, ti))
        E[ti].append((t - s, si))

    solver = Dijkstra(len(X), E, inf=1 << 60)
    cost = solver.cost_from(0)
    print(cost[-1])


if __name__ == "__main__":
    main()
