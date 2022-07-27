#!/usr/bin/env python3

def main():
    s = {n for n in range(1, 31)}
    for _ in range(28):
        s.remove(int(input()))
    for n in sorted(s):
        print(n)


if __name__ == "__main__":
    main()
