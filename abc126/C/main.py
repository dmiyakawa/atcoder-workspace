#!/usr/bin/env python3


def solve_2(N: int, K: int):
    ans = 0
    for n in range(1, N + 1):
        tmp = 1 / N
        while n < K:
            tmp *= 1 / 2
            n *= 2
        ans += tmp
    print(ans)


def solve(N: int, K: int):
    # 初AC
    lst = [max((N - K + 1), 0) / N]
    k = min(N, K - 1)
    if k > 0:
        i = 1
        while k * 2**i < K:
            i += 1

        while k > 0:
            cur_max = k
            cur_min = k // 2
            while True:
                cur_mid = (cur_min + cur_max) // 2
                # print(cur_mid, i)
                if cur_mid * 2**i < K:
                    if K <= (cur_mid + 1) * 2**i:
                        next_val = cur_mid
                        break
                    else:
                        cur_min = cur_mid
                else:
                    cur_max = cur_mid

            tmp = (k - next_val)/(N * 2**i)
            # print(k, next_val, i, f"{tmp:f}", sum(lst))
            lst.append(tmp)
            i += 1
            k = next_val
    lst.sort()
    print(sum(lst))


def main():
    N, K = map(int, input().split())
    solve_2(N, K)


if __name__ == "__main__":
    main()
