#!/usr/bin/env python3

MOD = 1000000007  # type: int


def main():
    import math
    N = int(input())
    T = sorted(int(input()) for _ in range(N))
    total_penalty = 0
    elapsed_time = 0
    prev_time = 0
    same_time_count = 1
    possible_combinations = 1
    for t in T:
        elapsed_time += t
        total_penalty += elapsed_time
        if prev_time == t:
            same_time_count += 1
        else:
            possible_combinations = (possible_combinations * math.factorial(same_time_count)) % MOD
            prev_time = t
            same_time_count = 1

    possible_combinations = (possible_combinations * math.factorial(same_time_count)) % MOD
    print(total_penalty)
    print(possible_combinations)



if __name__ == "__main__":
    main()
