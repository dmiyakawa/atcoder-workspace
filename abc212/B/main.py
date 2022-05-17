#!/usr/bin/env python3

def main():
    xs = [int(e) for e in input()]
    if xs[0] == xs[1] == xs[2] == xs[3]:
        print("Weak")
    elif (
            (xs[0] + 1) % 10 == xs[1]
            and (xs[1] + 1) % 10 == xs[2]
        and (xs[2] + 1) % 10 == xs[3]
    ):
        print("Weak")
    else:
        print("Strong")


if __name__ == "__main__":
    main()
