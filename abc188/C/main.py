#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [(s, i) for i, s in enumerate(A)]
    while len(B) > 2:
        next_b = []
        for i in range(len(B) // 2):
            a, b = 2 * i, 2 * i + 1
            next_b.append(B[a] if B[a][0] > B[b][0] else B[b])
        B = next_b
    print(min(B)[1] + 1)


if __name__ == "__main__":
    main()
