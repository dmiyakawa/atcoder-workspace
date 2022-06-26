#!/usr/bin/env python3

def main():
    N = int(input())
    nodes = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        nodes.append((x, y, p))

    min_s = 1
    max_s = 1
    # O(N^2)
    for i in range(N):
        src = nodes[i]
        src_p = src[2]
        for j in range(N):
            dst = nodes[j]
            cost = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
            max_s = max(cost // src_p + 1, max_s)

    mid_s = (min_s + max_s) // 2

    while max_s > min_s:
        d = [[] for _ in range(N)]
        for i in range(N):
            src = nodes[i]
            for j in range(N):
                dst = nodes[j]
                d[i].append(0 if i == j else max(abs(src[0] - dst[0]) + abs(src[1] - dst[1]) - src[2] * mid_s, 0))
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        min_cost = min(max(d[i]) for i in range(N))
        if min_cost == 0:
            max_s = mid_s
        else:
            min_s = mid_s + 1
        mid_s = (min_s + max_s) // 2
    print(mid_s)


if __name__ == "__main__":
    main()
