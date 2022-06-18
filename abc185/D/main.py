#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    A = sorted(int(e) - 1 for e in input().split()) if M > 0 else []
    w = []
    prev = -1
    for a in A:
        if a - prev > 1:
            w.append(a - 1 - prev)
        prev = a
    if N - prev > 1:
        w.append(N - 1 - prev)

    if not w:
        print(0)
        return
    k = min(w)
    ans = 0
    for seq in w:
        ans += seq // k + (1 if seq % k else 0)
    print(ans)


if __name__ == "__main__":
    main()
