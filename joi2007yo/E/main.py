#!/usr/bin/env python3

def main():
    num_a, num_b, num_c = map(int, input().split())
    N = int(input())
    exams = [tuple(int(e) for e in input().split()) for _ in range(N)]
    results = [2 for _ in range(num_a + num_b + num_c)]
    for _ in range(num_a + num_b + num_c):
        for i, j, k, r in exams:
            i, j, k = i-1, j-1, k-1
            if r == 1:
                results[i] = 1
                results[j] = 1
                results[k] = 1
            else:
                if results[i] == 1 and results[j] == 1:
                    results[k] = 0
                elif results[i] == 1 and results[k] == 1:
                    results[j] = 0
                elif results[j] == 1 and results[k] == 1:
                    results[i] = 0
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
