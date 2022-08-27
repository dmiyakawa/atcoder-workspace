#!/usr/bin/env python3

def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    lst = [(n, rate) for n, rate in enumerate(A, start=1)]
    while len(lst) > 2:
        new_lst = []
        for i in range(len(lst) // 2):
            new_lst.append(lst[2 * i] if lst[2 * i][1] > lst[2 * i + 1][1] else lst[2 * i + 1])
        lst = new_lst

    print(lst[0][0] if lst[0][1] < lst[1][1] else lst[1][0])


if __name__ == "__main__":
    main()
