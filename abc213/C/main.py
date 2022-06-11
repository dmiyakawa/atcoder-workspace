#!/usr/bin/env python3

def main():
    H, W, N = [int(e) for e in input().split()]
    lst = []
    for n in range(1, N + 1):
        h, w = [int(e) for e in input().split()]
        lst.append((h, w, n))
    d_w = {}
    last_h = 0
    empty_h = 0
    for h, w, n in sorted(lst):
        if last_h != h:
            empty_h += h - last_h - 1
            last_h = h
        d_w.setdefault(w, []).append((h - empty_h - 1, w - 1, n))
    lst = []
    for i, (w, values) in enumerate(sorted(d_w.items())):
        for h, w, n in values:
            lst.append((h, i, n))
    for h, i, _ in sorted(lst, key=lambda x: x[2]):
        print(h + 1, i + 1)


if __name__ == "__main__":
    main()
