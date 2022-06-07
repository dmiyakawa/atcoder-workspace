#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    S = input()
    l_count = 0
    r_count = 0
    while len(S) - r_count > 0 and S[len(S) - r_count - 1] == "a":
        r_count += 1
    if r_count == len(S):
        print(YES)
        return
    while l_count < len(S) and S[l_count] == "a":
        l_count += 1

    if l_count > r_count:
        print(NO)
        return

    S = S[l_count:len(S) - r_count]
    is_p = True
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - 1 - i]:
            is_p = False
            break
    print(YES if is_p else NO)


if __name__ == "__main__":
    main()
