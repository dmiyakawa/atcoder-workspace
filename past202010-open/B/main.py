#!/usr/bin/env python3

def solve(X, Y):
    if Y == 0:
        return "ERROR"
    else:
        return "{:.04f}".format(X / Y)[:-2]

def main():
    X, Y = map(int, input().split())
    print(solve(X, Y))


if __name__ == "__main__":
    main()
    # for a in range(101):
    #     for b in range(101):
    #         print(solve(a, b), a, b, (a / b if b != 0 else None))
