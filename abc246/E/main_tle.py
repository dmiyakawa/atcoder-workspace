#!/usr/bin/env python3
import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
INF = float("INF")


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A_x = int(next(tokens))  # type: int
    A_y = int(next(tokens))  # type: int
    B_x = int(next(tokens))  # type: int
    B_y = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    answer = solve(N, A_x, A_y, B_x, B_y, S)
    print(answer)


def solve(N: int, A_x: int, A_y: int, B_x: int, B_y: int, S: "List[str]"):
    A_x -= 1
    A_y -= 1
    B_x -= 1
    B_y -= 1
    visited_costs = {(A_x, A_y): 0}
    hq = [(0, A_x, A_y)]
    while hq:
        cost, x, y = heapq.heappop(hq)
        lt, lb, rt, rb = True, True, True, True
        for i in range(1, N):
            lst = []
            if lt:
                lst.append((x - i, y - i, "lt"))
            if lb:
                lst.append((x - i, y + i, "lb"))
            if rt:
                lst.append((x + i, y - i, "rt"))
            if rb:
                lst.append((x + i, y + i, "rb"))
            if not lst:
                break
            for (x_i, y_i, direction) in lst:
                if x_i < 0 or N <= x_i or y_i < 0 or N <= y_i or (x_i, y_i) in visited_costs:
                    continue
                if S[x_i][y_i] == "#":
                    if direction == "lt":
                        lt = False
                    elif direction == "lb":
                        lb = False
                    elif direction == "rt":
                        rt = False
                    else:
                        rb = False
                    continue
                new_cost = min(cost + 1, visited_costs.get((x_i, y_i), INF))
                visited_costs[(x_i, y_i)] = new_cost
                if (x_i, y_i) == (B_x, B_y):
                    return new_cost
                heapq.heappush(hq, (new_cost, x_i, y_i))
    return -1


if __name__ == "__main__":
    main()
