#!/usr/bin/env python3

import sys
from typing import List


class Node:
    def __init__(self, _id):
        self._id = _id
        self.staffs: List["Node"] = []

    def calc_salary(self):
        salaries = [staff.calc_salary() for staff in self.staffs]
        if salaries:
            return max(salaries) + min(salaries) + 1
        else:
            return 1


def solve(N: int, B: "List[int]"):
    takahashi = Node(1)
    members = [None, takahashi, *[Node(n) for n in range(2, N + 1)]]
    for n, b in enumerate(B, start=2):
        members[b].staffs.append(members[n])

    print(takahashi.calc_salary())


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(N - 2 + 1)]  # type: "List[int]"
    solve(N, B)


if __name__ == "__main__":
    main()
