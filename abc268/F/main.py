#!/usr/bin/env python3
import functools

def count(s):
    ret = 0
    x = 0
    for ch in s:
        if ch == "X":
            x += 1
        else:
            ret += x * int(ch)
    return ret


def solve(N: int, S: "List[str]"):
    X = [(s.count("X"), sum(int(ch) for ch in s if ch != "X"), i) for i, s in enumerate(S)]

    def cmp(a, b):
        return a[0] * b[1] - b[0] * a[1]

    X.sort(key=functools.cmp_to_key(cmp), reverse=True)
    lst = []
    for x in X:
        lst.append(S[x[2]])
    T = "".join(lst)
    # print(T)
    print(count(T))


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == "__main__":
    main()
