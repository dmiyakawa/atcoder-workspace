#!/usr/bin/env python3

def main():
    N, K = [int(e) for e in input().split()]
    S = input()
    print(S[:K-1] + S[K-1].lower() + S[K:])


if __name__ == "__main__":
    main()
