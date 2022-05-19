#!/usr/bin/env python3

def main():
    A, B, C = [int(e) for e in input().split()]
    is_plus = (A + B == C)
    is_minus = (A - B == C)
    if is_plus:
        if is_minus:
            print("?")
        else:
            print("+")
    else:
        if is_minus:
            print("-")
        else:
            print("!")


if __name__ == "__main__":
    main()
