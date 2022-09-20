#!/usr/bin/env python3


def solve_2(S: "List[str]"):
    a = 10**9
    b = -10**9
    c = 10**9
    d = -10**9
    for i, s in enumerate(S):
        for j, ch in enumerate(s):
            if ch == "#":
                a = min(a, i)
                b = max(b, i)
                c = min(c, j)
                d = max(d, j)
    print(a + 1, b + 1)
    print(c + 1, d + 1)


def solve(S: "List[str]"):
    a, b, c, d = -1, -1, -1, -1
    for i, s in enumerate(S):
        if "#" in s:
            if a < 0:
                a = i + 1
                for j, ch in enumerate(s):
                    if ch == "#" and c < 0:
                        c = j + 1
                    elif ch == "." and c >= 0:
                        d = j
                        break
                if d < 0:
                    d = len(s)
        else:
            if b < 0 and a >= 0:
                b = i
                break
    if b < 0:
        b = len(S)
    print(a, b)
    print(c, d)



def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(10)]  # type: "List[str]"
    solve_2(S)


if __name__ == "__main__":
    main()
