#!/usr/bin/env python3

Inf = INF = float("INF")

def solve(N: int, W: int, C: int, l: "List[int]", r: "List[int]", p: "List[int]"):
    up, down = {0: 0}, {0: 0}
    keys = {0}
    for l0, r0, p0 in zip(l, r, p):
        up[l0] = up.get(l0, 0) + p0
        down[r0] = down.get(r0, 0) + p0
        keys.add(l0)
        keys.add(r0)
    sorted_pos = sorted(keys)
    l_index = 0
    r_index = 0
    min_p = sum(p)
    cur_p = 0
    while r_index < len(sorted_pos):
        while r_index < len(sorted_pos) and sorted_pos[r_index] - sorted_pos[l_index] < C:
            cur_p += up.get(sorted_pos[r_index], 0)
            r_index += 1
        right = sorted_pos[r_index] if r_index < len(sorted_pos) else W
        if right - sorted_pos[l_index] >= C:
            min_p = min(min_p, cur_p)
        while l_index < r_index and right - sorted_pos[l_index] >= C:
            l_index += 1
            left = sorted_pos[l_index] if l_index < len(sorted_pos) else W
            cur_p -= down.get(left, 0)
            if right - left >= C:
                min_p = min(min_p, cur_p)
    print(min_p)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    p = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
        p[i] = int(next(tokens))
    solve(N, W, C, l, r, p)


if __name__ == "__main__":
    main()
