#!/usr/bin/env python3


def solve(A: int, B: int, C: int, D: int, E: int, F: int):
    max_s = None
    max_sugar = 0
    max_water = 0
    for b in range(31):
        for a in range(31):
            if a == 0 and b == 0:
                continue
            water = a * A + b * B
            water_100 = water * 100
            remaining = F - water_100
            if remaining < 0 or (max_s is not None and max_s > remaining / F):
                continue
            for c in range(remaining // C + 1):
                for d in range((remaining - c * C) // D + 1):
                    sugar = c * C + d * D
                    total = sugar + water_100
                    assert total <= F
                    if E * water < sugar:
                        continue
                    if max_s is None or max_s < sugar/(sugar + water_100):
                        # print(max_s, sugar, sugar + water_100, sugar/(sugar + water_100))
                        max_s = sugar/(sugar + water_100)
                        max_sugar = sugar
                        max_water = water_100
    print(max_water + max_sugar, max_sugar)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F)


if __name__ == "__main__":
    main()
