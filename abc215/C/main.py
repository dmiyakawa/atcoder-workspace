#!/usr/bin/env python3

import itertools


def main():
    S, K = input().split()
    K = int(K)
    print(sorted({"".join(perm) for perm in itertools.permutations(S)})[K - 1])


if __name__ == "__main__":
    main()
