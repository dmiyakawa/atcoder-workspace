#!/usr/bin/env python3

def _count(R, C, rows, index_to_flip):
    ret = 0
    for i in range(C):
        c0, c1 = 0, 0
        for j in range(R):
            if rows[j][i] == (1 if (index_to_flip >> j & 1) else 0):
                c0 += 1
            else:
                c1 += 1
        ret += max(c0, c1)
    return ret


def main():
    R, C = map(int, input().split())
    rows = [[int(e) for e in input().split()] for _ in range(R)]
    max_count = 0
    for index_to_flip in range(2**R):
        max_count = max(max_count, _count(R, C, rows, index_to_flip))
    print(max_count)


if __name__ == "__main__":
    main()
