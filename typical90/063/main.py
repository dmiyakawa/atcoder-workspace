#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    P = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, P)


def solve(H: int, W: int, P: "List[List[int]]"):
    max_num = 0
    for h in range(1, 2**H):
        p = [lst for i, lst in enumerate(P) if h & (1 << i)]
        d = {}
        for x in range(W):
            val = p[0][x]
            if all(lst[x] == val for lst in p):
                d[val] = d.get(val, 0) + 1
        if d:
            max_num = max(max_num, len(p) * max(d.values()))
    print(max_num)


if __name__ == "__main__":
    main()
