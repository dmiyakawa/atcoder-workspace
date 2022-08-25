#!/usr/bin/env python3

def solve(S: str, K: int):
    lst = []
    count = 0
    for i, ch in enumerate(S):
        if ch == "X":
            count += 1
        else:
            lst.append(count)
            count = 0
    lst.append(count)
    # print(S, K)
    # print(lst)

    r = 0
    cur = 0
    ans = 0
    for l in range(len(lst)):
        if l == 0:
            r = min(K + 1, len(lst))
            ans = cur = sum(lst[:r]) + r - 1
            # print(l, r, cur)
        else:
            cur -= lst[l - 1] + (1 if l < len(lst) else 0)
            if r < len(lst):
                cur += lst[r] + 1
                r += 1
            # print(l, r, cur)
            ans = max(ans, cur)
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
