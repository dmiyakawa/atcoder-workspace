#!/usr/bin/env python3

def main():
    Ns, S = input().split()
    print(solve(int(Ns), S))


def solve(N, S):
    s = [0 for _ in range(N)]
    for i, ch in enumerate(S):
        s[i] = 0 if ch == "A" else (1 if ch == "T" else (2 if ch == "C" else 3))
    count = 0
    for i in range(N):
        at = 1 if s[i] == 0 else (-1 if s[i] == 1 else 0)
        cg = 1 if s[i] == 2 else (-1 if s[i] == 3 else 0)
        for j in range(i + 1, N):
            at += 1 if s[j] == 0 else (-1 if s[j] == 1 else 0)
            cg += 1 if s[j] == 2 else (-1 if s[j] == 3 else 0)
            # print(f"i: {i}, j: {j}, at: {at}, cg: {cg}")
            if at == 0 and cg == 0:
                count += 1

    return count


def debug():
    # S = "AT" * 1250 + "GC" * 1250
    S = "AT" * 2500
    print(solve(len(S), S))


if __name__ == "__main__":
    # debug()
    main()
