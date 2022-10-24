#!/usr/bin/env python3



def main():
    H, W = map(int, input().split())
    ans = [0] * W
    for _ in range(H):
        line = list(input())
        for i in range(W):
            if line[i] == "#":
                ans[i] += 1
    print(*ans)


if __name__ == "__main__":
    main()
