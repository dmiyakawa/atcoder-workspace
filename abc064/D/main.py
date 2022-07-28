#!/usr/bin/env python3

def main():
    N = int(input())
    S = input()
    stack = []
    for i, ch in enumerate(S):
        if ch == "(":
            stack.append(i)
        elif ch == ")" and stack:
            stack.pop()

    S = S + ")" * len(stack)

    stack = []
    for i, ch in enumerate(reversed(S)):
        if ch == ")":
            stack.append(i)
        elif ch == "(":
            stack.pop()
    S = "(" * len(stack) + S
    print(S)


if __name__ == "__main__":
    main()
