#!/usr/bin/env python3
#
# 注意すべき例, Sb = "?b??", T = "ab"
#

def main():
    Sd = input()
    T = input()
    cands = []
    for i in range(len(Sd) - len(T) + 1):
        successful = True
        for j, ch in enumerate(T):
            if Sd[i + j] != "?" and Sd[i + j] != ch:
                successful = False
                break
        if successful:
            s = Sd[:i] + T + Sd[i + len(T):]
            cands.append(s.replace("?", "a"))
    if cands:
        print(sorted(cands)[0])
    else:
        print("UNRESTORABLE")


def main_re():
    # 正規表現を使った逃げ解法
    import re
    Sd = input()
    T = input()
    Ts = "".join(["[{}?]".format(ch) for ch in T])
    cands = []
    for i in range(len(Sd) - len(T) + 1):
        s = (Sd[:i] + re.sub(Ts, T, Sd[i:])).replace("?", "a")
        if T in s:
            cands.append(s)
    if cands:
        print(sorted(cands)[0])
    else:
        print("UNRESTORABLE")


if __name__ == "__main__":
    main()
