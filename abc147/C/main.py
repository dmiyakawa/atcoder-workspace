#!/usr/bin/env python3


def main():
    N = int(input())
    answers = [[] for _ in range(N)]
    for i in range(N):
        A = int(input())
        for _ in range(A):
            x, y = [int(e) for e in input().split()]
            answers[i].append((x - 1, y))

    possible_nums = set()
    for n in range(2**N - 1, -1, -1):
        d = {i: answers[i] for i in range(N) if (n // 2 ** i) % 2 == 1}

        possible = True
        for key, values in d.items():
            for x, y in values:
                if y == 0 and x in d or y == 1 and x not in d:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_nums.add(format(n, "b").count("1"))
    print(max(possible_nums))


if __name__ == "__main__":
    main()
