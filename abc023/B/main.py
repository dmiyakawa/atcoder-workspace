#!/usr/bin/env python3


def solve(S) -> int:
    if len(S) % 2 == 0:
        return -1
    mid = len(S) // 2
    count = 0
    while mid + count < len(S):
        s = S[mid - count] + S[mid + count]
        if (count % 3 == 0 and s == "bb"
                or count % 3 == 1 and s == "ac"
                or count % 3 == 2 and s == "ca"):
            count += 1
        else:
            return -1
    return count - 1


def main():
    input()
    S = input()
    print(solve(S))


def main_a():
    N = int(input())
    S = input()
    offset = -1
    if S[0] == S[-1] == "b":
        offset = 0
    elif S[0] == "a" and S[-1] == "c":
        offset = 2
    elif S[0] == "c" and S[-1] == "a":
        offset = 1
    if offset == -1:
        print(-1)
        return

    count = 0
    while len(S) > 1:
        if (count + offset) % 3 == 0 and S[0] == S[-1] == "b":
            count += 1
        elif (count + offset) % 3 == 2 and S[0] == "a" and S[-1] == "c":
            count += 1
        elif (count + offset) % 3 == 1 and S[0] == "c" and S[-1] == "a":
            count += 1
        else:
            print(-1)
            return
        S = S[1:-1]
    print(count if S == "b" else -1)


if __name__ == "__main__":
    main()
