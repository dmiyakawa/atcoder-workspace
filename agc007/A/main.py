#!/usr/bin/env python3

YES = "Possible"  # type: str
NO = "Impossible"  # type: str


def main():
    H, W = map(int, input().split())
    count = 0
    for _ in range(H):
        count += input().count("#")
    print(YES if count == H + W - 1 else NO)


if __name__ == "__main__":
    main()
