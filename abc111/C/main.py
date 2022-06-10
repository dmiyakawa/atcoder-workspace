#!/usr/bin/env python3
from typing import Any


def main():
    from collections import Counter
    n = int(input())
    v = [int(e) for e in input().split()]
    ce: Any = sorted(Counter(v[::2]).items(), key=lambda x: x[1], reverse=True)
    co: Any = sorted(Counter(v[1::2]).items(), key=lambda x: x[1], reverse=True)

    select_ce: bool
    if ce[0] == co[0]:
        if ce[0][1] == n // 2:
            print(n // 2)
            return
        select_ce = ce[1][1] < co[1][1]
    else:
        select_ce = ce[0][1] > co[0][1]

    if select_ce:
        ne = n // 2 - ce[0][1]
        no = n // 2
        for key, value in co:
            if key != ce[0][0]:
                no = n // 2 - value
                break
    else:
        ne = n // 2
        no = n // 2 - co[0][1]
        for key, value in ce:
            if key != co[0][0]:
                ne = n // 2 - value
                break

    print(ne + no)


if __name__ == "__main__":
    main()
