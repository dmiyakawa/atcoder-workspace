#!/usr/bin/env python3

def main():
    input()
    S = input()
    left, right = 0, len(S) - 1
    count = 0
    while left < right:
        if S[left] == "R":
            left += 1
        elif S[right] == "W":
            right -= 1
        else:
            left += 1
            right -= 1
            count += 1
    print(count)


if __name__ == "__main__":
    main()
