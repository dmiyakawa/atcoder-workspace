#!/usr/bin/env python3

def main():
    print(solve(input()))


def solve(s: str):
    import functools
    allowed = [{ch} for ch in s]
    for i in range(len(s)):
        intersection = functools.reduce(lambda x, y: x & y, allowed)
        if intersection:
            return i
        for j in range(len(allowed) - 1):
            allowed[j] |= allowed[j + 1]
        allowed.pop()


if __name__ == "__main__":
    main()
