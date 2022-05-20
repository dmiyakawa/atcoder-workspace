#!/usr/bin/env python3

def main():
    input()
    A = [int(e) for e in input().split()]
    cut_radiuses = {0}
    current_rot = 0
    for a in A:
        current_rot = (current_rot + a) % 360
        cut_radiuses.add(current_rot)
    max_diff = 0
    prev_rot = 0
    for rot in sorted(cut_radiuses):
        max_diff = max(rot - prev_rot, max_diff)
        prev_rot = rot
    max_diff = max(360 - prev_rot, max_diff)
    print(max_diff)


if __name__ == "__main__":
    main()
