#!/usr/bin/env python3


def solve(S: str, T: str):
    si, ti = 0, 0
    while si < len(S) or ti < len(T):
        if si == len(S) or ti == len(T):
            return False
        ch_s = S[si]
        ch_t = T[ti]
        if ch_s != ch_t:
            return False
        len_s = 0
        len_t = 0
        while si < len(S) and S[si] == ch_s:
            si += 1
            len_s += 1
        while ti < len(T) and T[ti] == ch_t:
            ti += 1
            len_t += 1
        if len_s != len_t and (len_s > len_t or len_s < 2):
            return False

    return True


def main():
    S = input().rstrip()
    T = input().rstrip()
    print("Yes" if solve(S, T) else "No")


if __name__ == "__main__":
    main()
