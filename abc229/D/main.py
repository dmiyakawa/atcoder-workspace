#!/usr/bin/env python3

def solve(S: str, K: int):
    lst = []
    num = 0
    for ch in S:
        if ch == ".":
            lst.append(num)
            num = 0
        else:
            num += 1
    lst.append(num)
    ans = max(lst)
    print(lst)
    cur = 0
    for l in range(len(lst)):
        r = l + K + 1
        if l == 0:
            cur = sum(lst[l:min(r, len(lst))])
        else:
            cur -= lst[l - 1]
            if r < len(lst):
                cur += lst[r]
            else:
                r = len(lst)
        print(l, r, lst[l:r], cur + r - l - 1)
        ans = max(ans, cur + r - l - 1)
    print(ans)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)




if __name__ == "__main__":
    main()
