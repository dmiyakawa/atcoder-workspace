#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        val = int(input())
        if val == 0:
            return N
        S.append(val)
    if K == 0:
        return 0
    left = 0
    max_length = 0
    product = 1
    for right, val in enumerate(S):
        product *= val
        if product > K:
            while product > K and left <= right:
                product //= S[left]
                left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    print(main())
