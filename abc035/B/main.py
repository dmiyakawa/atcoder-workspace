#!/usr/bin/env python3


def main():
    S = input()
    T = int(input())
    x, y = 0, 0
    num_questions = 0
    d = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
    for ch in S:
        if ch == "?":
            num_questions += 1
        else:
            x, y = x + d[ch][0], y + d[ch][1]
    if T == 1:
        print(abs(x) + abs(y) + num_questions)
    else:
        for _ in range(num_questions):
            if y > 0:
                y -= 1
            elif y < 0:
                y += 1
            elif x > 0:
                x -= 1
            else:
                x += 1
        print(abs(x) + abs(y))


if __name__ == "__main__":
    main()
