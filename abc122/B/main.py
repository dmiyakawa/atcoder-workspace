#!/usr/bin/env python3

def main():
    S = input()
    max_count = 0
    count = 0
    for i, ch in enumerate(S):
        if ch in "ACGT":
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    max_count = max(count, max_count)
    print(max_count)


if __name__ == "__main__":
    main()
