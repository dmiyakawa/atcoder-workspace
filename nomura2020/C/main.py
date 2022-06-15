#!/usr/bin/env python3

def solve(N, A):
    total_nodes = 0
    num_current_nodes = 1
    num_remaining_leafs = sum(A)
    for i, a in enumerate(A):
        if a > num_current_nodes or num_current_nodes > num_remaining_leafs:
            return -1
        total_nodes += num_current_nodes
        num_current_nodes -= a
        num_remaining_leafs -= a
        num_current_nodes = min(num_current_nodes * 2, num_remaining_leafs)
    return total_nodes


def main():
    N = int(input())
    A = [int(e) for e in input().split()]
    print(solve(N, A))


if __name__ == "__main__":
    main()
