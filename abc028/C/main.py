#!/usr/bin/env python3

def main():
    from itertools import combinations
    lst = [int(e) for e in input().split()]
    print(sorted((sum(tup)for tup in combinations(lst, 3)), reverse=True)[2])


if __name__ == "__main__":
    main()
