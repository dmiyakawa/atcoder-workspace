#!/usr/bin/env python3

def main():
    lst = []
    for ch in input():
        if ch == "B":
            if lst:
                lst.pop()
        else:
            lst.append(ch)
    print("".join(lst))


if __name__ == "__main__":
    main()
