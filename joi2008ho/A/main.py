#!/usr/bin/env python3

def main():
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    res = []
    for i, n in enumerate(lst):
        if i % 2 == 0:
            if res and res[-1][0] == n:
                res[-1] = (n, res[-1][1] + 1)
            else:
                res.append((n, 1))
        else:
            if res:
                res[-1] = (n, res[-1][1] + 1)
                if len(res) > 1 and res[-2][0] == res[-1][0]:
                    num = res[-2][1] + res[-1][1]
                    res.pop()
                    res[-1] = (n, num)
            else:
                res.append((n, 1))
    ans = 0
    for n, c in res:
        if n == 0:
            ans += c
    print(ans)


if __name__ == "__main__":
    main()
