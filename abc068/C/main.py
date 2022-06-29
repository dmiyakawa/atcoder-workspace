from collections import defaultdict

N, M = map(int, input().split())
d = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)

visited = set()
to_visit = {(1, 0)}
while to_visit:
    node, hop = to_visit.pop()
    if node in visited:
        continue
    visited.add(node)
    if hop < 2:
        for next_node in d[node]:
            to_visit.add((next_node, hop + 1))
print("POSSIBLE" if N in visited else "IMPOSSIBLE")
