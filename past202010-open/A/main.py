#!/usr/bin/env python3

def main():
    print({0: "A", 1: "B", 2: "C"}[sorted(enumerate(int(e) for e in input().split()), key=lambda tup: tup[1])[1][0]])

if __name__ == "__main__":
    main()
