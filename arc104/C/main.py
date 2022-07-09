#!/usr/bin/env python3

def main():
    N = int(input())
    s = set()
    # 0-origin
    A, B, AB = [], [], []
    certain_ab = []
    uncertain_downward = []
    uncertain_upward = []
    num_wild_card = 0
    for i in range(N):
        a, b = [int(e) - 1 for e in input().split()]
        A.append(a)
        B.append(b)
        AB.append((a, b))
        if a > 0:
            if a in s:
                return False
            s.add(a)
            if b > 0:
                certain_ab.append((a, b, i))
            else:
                uncertain_upward.append((a, i))
        else:
            if b < 0:
                num_wild_card += 1

        if b > 0:
            if b in s:
                return False
            s.add(b)
            if a < 0:
                uncertain_downward.append((b, i))

        if a > b > 0:
            return False

    ...

    return True


if __name__ == "__main__":
    print("Yes" if main() else "No")
