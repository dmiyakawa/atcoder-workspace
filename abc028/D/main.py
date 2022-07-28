#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    if N == 1:
        c = 1
    elif K == 0:
        c = (N - K)*3 + 1
    elif K == N:
        c = (K - 1) * 3
    else:
        c = (K - 1)*(N - K)*3*2 + (K - 1) * 3 + (N - K)*3 + 1
    print(c/N**3)



if __name__ == "__main__":
    main()
