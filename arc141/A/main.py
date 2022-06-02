#!/usr/bin/env python3


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        strN = str(N)
        lenN = len(strN)
        max_value = 0
        for i in range(2, lenN + 1):
            if lenN % i == 0:
                # print("*", lenN//i)
                part = strN[:lenN//i]
                part_int = int(part)
                part_int_tail = part_int % 10
                for j in range(part_int_tail, -1, -1):
                    part2_int = (part_int // 10) * 10 + j
                    part2 = str(part2_int)
                    value = int(part2 * i)
                    if value <= N:
                        # print("*", value, max(max_value, value))
                        max_value = max(max_value, value)
                        break
        print(max_value)


if __name__ == "__main__":
    main()
