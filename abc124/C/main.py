#!/usr/bin/env python3

def main():
    S = input()
    a = sum(1 if int(ch) == i % 2 else 0 for i, ch in enumerate(S))
    b = sum(1 if int(ch) == (i + 1) % 2 else 0 for i, ch in enumerate(S))
    print(min(a, b))


if __name__ == "__main__":
    main()
