#!/usr/bin/env python3

def solve(H, W, C) -> int:
    dp = [[0 for _ in range(W)] for _ in range(H)]
    for j in range(W):
        dp[0][j] = (1 if C[0][j] == 0 else 0)
    for i in range(1, H):
        for j in range(W):
            dp[i][j] = dp[i - 1][j] + 1 if C[i][j] == 0 else 0
    ans = 0
    for i in range(H):
        st = []
        for j in range(W):
            h0 = dp[i][j]
            if not st or st[-1][1] < h0:
                st.append((j, h0))
            elif st[-1][1] > h0:
                new_p = j
                while st and st[-1][1] >= h0:
                    p, h = st.pop()
                    ans = max(ans, (j - p) * h)
                    new_p = p
                st.append((new_p, h0))
        while st:
            p, h = st.pop()
            ans = max(ans, (W - p) * h)

    return ans


def main():
    H, W = map(int, input().split())
    C = [[int(e) for e in input().split()] for _ in range(H)]
    print(solve(H, W, C))


if __name__ == "__main__":
    main()
