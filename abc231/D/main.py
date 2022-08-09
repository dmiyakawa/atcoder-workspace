#!/usr/bin/env python3
from collections import defaultdict

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    links = defaultdict(set)
    for a, b in zip(A, B):
        links[a].add(b)
        links[b].add(a)
        if len(links[a]) > 2 or len(links[b]) > 2:
            print("No")
            return
    shown = set()
    for i in range(N):
        if i in shown:
            continue
        to_visit = {(link, i) for link in links[i]}
        while to_visit:
            n, prev = to_visit.pop()
            if n in shown:
                print("No")
                return
            shown.add(n)
            for link in links[n]:
                if link != prev:
                    to_visit.add((link, n))
    print("Yes")


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)





if __name__ == "__main__":
    main()
