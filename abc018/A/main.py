#!/usr/bin/env python3

def main():
    lst = [int(input()), int(input()), int(input())]
    s_lst = sorted(lst, reverse=True)
    for n in lst:
        print(s_lst.index(n) + 1)


if __name__ == "__main__":
    main()
