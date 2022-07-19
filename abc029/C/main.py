#!/usr/bin/env python3


def main2():
    N = int(input())
    for i in range(3**N):
        print("".join("abc"[(i // 3 ** j) % 3] for j in range(N - 1, -1, -1)))




def main():
    from itertools import product
    N = int(input())
    for p in product(*["abc" for _ in range(N)]):
        print("".join(p))


if __name__ == "__main__":
    main2()
