#!/usr/bin/env python3

def solve(S: str):
    s = []
    lst = []
    c = 0
    for ch in S:
        lst.append(ch)
        if ch.isupper():
            c += 1
            if c == 2:
                s.append("".join(lst))
                c = 0
                lst = []
    print("".join(sorted(s, key=lambda st: st.lower())))



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)



if __name__ == "__main__":
    main()
