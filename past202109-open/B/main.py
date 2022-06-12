#!/usr/bin/env python3

def main():
    N, M = [int(e) for e in input().split()]
    A = {a for a in [int(e) for e in input().split()]}
    B = {b for b in [int(e) for e in input().split()]}
    print(*sorted(A & B))


if __name__ == "__main__":
    main()
