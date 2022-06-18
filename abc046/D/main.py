#!/usr/bin/env python3

def main():
    s = input()
    score = 0
    for i, t in enumerate(s):
        a = "g" if i % 2 == 0 else "p"
        if t < a:
            score += 1
        elif t > a:
            score -= 1
    print(score)


if __name__ == "__main__":
    main()
