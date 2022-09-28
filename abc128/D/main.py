#!/usr/bin/env python3

def solve(N: int, K: int, V: "List[int]"):
    ans = 0
    for left in range(min(K + 1, N + 1)):
        for right in range(min(K + 1, N + 1) - left):
            lst = []
            for i in range(left):
                lst.append(V[i])
            for i in range(right):
                lst.append(V[-1 - i])
            lst.sort(reverse=True)
            rem = K - left - right
            while rem > 0 and lst and lst[-1] < 0:
                lst.pop()
                rem -= 1
            ans = max(ans, sum(lst))
    print(ans)


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, V)


if __name__ == "__main__":
    main()
