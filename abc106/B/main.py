#!/usr/bin/env python3

def main():
    N = int(input())
    count = 0
    for n in range(1, N + 1, 2):
        num_divisors = 0
        for i in range(1, n + 1):
            if n % i == 0:
                num_divisors += 1
        if num_divisors == 8:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
