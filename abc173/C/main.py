#!/usr/bin/env python3

def main():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    count = 0
    for mask_h in range(2**H):
        for mask_w in range(2**W):
            num_black = 0
            for h in range(H):
                if 1 << h & mask_h:
                    continue
                for w in range(W):
                    if 1 << w & mask_w:
                        continue
                    if C[h][w] == "#":
                        num_black += 1
            if num_black == K:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
