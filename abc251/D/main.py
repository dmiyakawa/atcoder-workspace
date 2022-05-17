#!/usr/bin/env python3

def construct(W):
    lst = []
    for n in range(0, 3):
        for i in range(1, 100):
            value = i * 100**n
            if value > W:
                return lst
            lst.append(value)
    return lst


def main():
    W = int(input())
    lst = construct(W)
    print(len(lst))
    print(*lst)


if __name__ == "__main__":
    main()

