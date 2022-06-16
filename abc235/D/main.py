#!/usr/bin/env python3

import math
from typing import Dict

def main():
    a, N = map(int, input().split())
    possibles: Dict[int, float] = {N: 0}
    to_visit = {N}
    visited = set()
    while to_visit:
        n = to_visit.pop()
        visited.add(n)
        if n % a == 0:
            v = n // a
            if v not in possibles or possibles.get(v, math.inf) > possibles[n] + 1:
                possibles[v] = min(possibles[n] + 1, possibles.get(v, math.inf))
                to_visit.add(v)

        s = str(n)
        rots = s[1:] + s[0]
        if rots[0] != "0":
            v = int(rots)
            if v not in possibles or possibles.get(v, math.inf) > possibles[n] + 1:
                possibles[v] = possibles[n] + 1
                to_visit.add(v)
    print(possibles.get(1, -1))


if __name__ == "__main__":
    main()
