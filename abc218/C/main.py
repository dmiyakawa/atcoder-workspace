#!/usr/bin/env python3

import sys

def match(S, Ts, h, w):
    len_h = len(Ts)
    len_w = len(Ts[0])
    for i in range(len(S)):
        for j in range(len(S[0])):
            if i < h or h + len_h <= i or j < w or w + len_w <= j:
                if S[i][j] == "#":
                    return False
            else:
                if S[i][j] != Ts[i - h][j - w]:
                    return False
    return True


def rot(Ts):
    h = len(Ts[0])
    w = len(Ts)
    ret = []
    for i in range(h):
        lst = []
        for j in range(w):
            lst.append(Ts[w - j - 1][i])
        ret.append("".join(lst))
    return ret


def solve(N: int, S: "List[str]", T: "List[str]"):
    top = -1
    bottom = -1
    left = 10000
    right = -1
    for i, t in enumerate(T):
        l, r = t.find("#"), t.rfind("#")
        if l >= 0:
            if top < 0:
                top = i
            left = min(left, l)
            right = max(right, r + 1)
        else:
            if bottom < 0 <= top:
                bottom = i
                break
    if bottom < 0:
        bottom = N
    Ts = [t[left:right] for t in T[top:bottom]]
    ts_h = len(Ts)
    ts_w = len(Ts[0])
    # print("\n".join(S) + "\n")

    for i in range(4):
        # print("\n".join(Ts) + "\n")
        for h in range(N - ts_h + 1):
            for w in range(N - ts_w + 1):
                # print(ts_h, ts_w, h, w)
                if match(S, Ts, h, w):
                    print("Yes")
                    return
        Ts = rot(Ts)
        ts_h = len(Ts)
        ts_w = len(Ts[0])
    print("No")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    T = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S, T)


if __name__ == "__main__":
    main()
