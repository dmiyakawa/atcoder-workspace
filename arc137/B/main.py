#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"

    max_nums = [0, 0]
    current_nums = [0, 0]
    for a in A:
        b = (a + 1) % 2
        current_nums[a] += 1
        max_nums[a] = max(max_nums[a], current_nums[a])
        if current_nums[b] > 0:
            current_nums[b] -= 1
    print(max_nums[0] + max_nums[1] + 1, end="")


if __name__ == "__main__":
    main()
