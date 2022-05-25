#!/usr/bin/env python3

def main():
    S = input()[:-1]
    while S:
        if len(S) % 2 == 0 and S[:len(S)//2] == S[len(S)//2:]:
            print(len(S))
            return
        S = S[:-1]


if __name__ == "__main__":
    main()
