#!/usr/bin/env python3


def main():
    input()
    As = [int(e) for e in input().split()]
    ans = 1
    if 0 in As:
        print(0)
        return
    for a in As:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)


if __name__ == "__main__":
    main()
