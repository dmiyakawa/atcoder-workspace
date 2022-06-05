#!/usr/bin/env python3

def main():
    N, M = [int(e) for e in input().split()]
    nodes = [set() for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) - 1 for e in input().split()]
        nodes[a].add(b)
        nodes[b].add(a)
    Q = int(input())
    for _ in range(Q):
        x_1, k = [int(e) for e in input().split()]
        x = x_1 - 1
        prev_s = None
        s = {x}
        # 各頂点の次数は3以下、かつ 0<=k_i<=3 なので最大でも考えるべきノード数は3**3=27くらい。定数とみなしてOK
        for _ in range(k):
            if prev_s == s:
                break
            prev_s = s
            for n_i in list(s):
                s = s.union(nodes[n_i])
        # nodeのindexを1ずつ減らしているので回答ではその分を戻すために len(s) 足す
        print(sum(s) + len(s))


if __name__ == "__main__":
    main()
