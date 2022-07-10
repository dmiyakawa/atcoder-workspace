#!/usr/bin/env python3

def main2():
    # 解説の想定解法
    # N = 12 ならば 4096 * 12 回のループ
    N, M = map(int, input().split())
    links = [1 << i for i in range(N)]
    for _ in range(M):
        x, y = [int(e) - 1 for e in input().split()]
        links[x] |= 1 << y
        links[y] |= 1 << x
    # for i, link in enumerate(links):
    #     print(i, format(link, "b"))

    max_size = 1
    for v in range(2 ** N):
        possible = True
        for i in range(N):
            if (v & 1 << i) and (links[i] & v != v):
                possible = False
                break
        if possible:
            max_size = max(max_size, format(v, "b").count("1"))
    print(max_size)


def possible_group_size(N, links, cur_members, i):
    max_size = format(cur_members, "b").count("1")
    if links[i] & cur_members == cur_members:
        max_size += 1
        for j in range(i + 1, N):
            max_size = max(possible_group_size(N, links, cur_members | (1 << i), j), max_size)
    return max_size


def main():
    N, M = map(int, input().split())
    links = [0 for _ in range(N)]
    for _ in range(M):
        x, y = [int(e) - 1 for e in input().split()]
        links[x] |= 1 << y
        links[y] |= 1 << x

    max_size = 1
    for i in range(N):
        for j in range(i + 1, N):
            max_size = max(possible_group_size(N, links, 1 << i, j), max_size)
    print(max_size)


if __name__ == "__main__":
    # main()
    main2()
