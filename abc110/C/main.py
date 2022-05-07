#!/usr/bin/env python3

import string


def main():
    S = input()  # type: str
    T = input()  # type: str
    print("Yes" if check(S, T) else "No")


def check(S, T):
    mapping = {ch: ch for ch in string.ascii_lowercase}
    appeared = set()
    for i in range(0, len(S)):
        s_i = mapping[S[i]]
        t_i = T[i]
        if s_i != t_i:
            if S[i] != s_i:
                return False
            if t_i in appeared:
                return False
            mapping[s_i] = t_i
        appeared.add(t_i)

    return True


if __name__ == "__main__":
    main()
