#!/usr/bin/env python3

def main():
    S = input()
    K = int(input())
    ans = "?"
    for i, ch in enumerate(S):
        if i == K - 1:
            ans = ch
            break
        elif ch != "1":
            ans = ch
            break
    print(ans)


if __name__ == "__main__":
    main()
