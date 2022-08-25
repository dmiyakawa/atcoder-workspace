#!/usr/bin/env python3


def solve(H: int, W: int):
    if H % 3 == 0 or W % 3 == 0:
        print(0)
        return
    ans = min(H, W)
    for h in range(max(1, H // 2), min(H, H // 2 + 1)):
        for w in range(max(1, W // 3 - 1), min(W, W // 3 + 2)):
            a = h * (W - w)
            b = (H - h) * (W - w)
            c = H * w
            ans = min(ans, max(a, b, c) - min(a, b, c))

    for w in range(max(1, W // 2), min(W, W // 2 + 1)):
        for h in range(max(1, H // 3 - 1), min(H, H // 3 + 2)):
            a = w * (H - h)
            b = (W - w) * (H - h)
            c = W * h
            ans = min(ans, max(a, b, c) - min(a, b, c))
    print(ans)


def main():
    import sys

    sys.setrecursionlimit(2 * (10 ** 5))

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(H, W)


if __name__ == "__main__":
    main()
