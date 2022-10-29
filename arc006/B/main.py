#!/usr/bin/env python3



def main():
    N, L = map(int, input().split())
    pos = [i for i in range(N)]
    for _ in range(L):
        line = input()
        for i in range(N - 1):
            if line[1 + 2 * i] == "-":
                pos[i], pos[i + 1] = pos[i + 1], pos[i]
    # print(pos)
    line = input()
    print(pos[line.index("o") // 2] + 1)



if __name__ == "__main__":
    main()
