#!/usr/bin/env python3



def solve(K: int):

    def backtrack(_j, _k, _count, ans_lst):
        # print("bt", _j, _k, _count, ans_lst)
        ans_lst.append(_j)
        lst.pop()
        if not lst:
            return sum(n * 10**i for i, n in enumerate(reversed(ans_lst)))
        _k -= _count
        ic = 0
        for l in range(-1, 2):
            if 0 <= _j + l <= 9:
                # print("  l", l, _j + l, lst[-1][_j + l])
                if ic + lst[-1][_j + l] >= _k:
                    return backtrack(_j + l, _k, ic, list(ans_lst))
                ic += lst[-1][_j + l]


    if K <= 9:
        return K

    lst = [[1] * 10]
    count = 9
    while True:
        lst.append([0] * 10)
        for j in range(10):
            assert count < K
            cc = lst[-2][j]
            if j > 0:
                cc += lst[-2][j - 1]
            if j < 9:
                cc += lst[-2][j + 1]
            lst[-1][j] = cc
            if j != 0:
                if count + cc >= K:
                    return backtrack(j, K, count, [])
                count += cc
            # print(len(lst), j, count, K)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    print(solve(K))


if __name__ == "__main__":
    main()
