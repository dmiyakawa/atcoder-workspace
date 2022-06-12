#!/usr/bin/env python3

def main():
    N = int(input())
    s = {n for n in range(1, N + 1)}
    dup = 0
    for _ in range(N):
        a = int(input())
        if a not in s:
            dup = a
        else:
            s.remove(a)
    if dup == 0:
        print("Correct")
    else:
        print(dup, s.pop())


if __name__ == "__main__":
    main()
