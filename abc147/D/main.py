#!/usr/bin/env python3


MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    """初AC推敲版。アルゴリズムは公式解説と同じ"""
    B = 0
    for a in A:
        b = 0
        while a:
            a >>= 1
            b += 1
        B = max(B, b)

    # 各桁の1の数を記憶する
    # (上のループとマージできそうだが分かりづらいし計算量変わらないのでこれで)
    bits = [0] * B
    for a in A:
        for j in range(B):
            bits[j] += (a >> j) & 1

    ans = 0
    for i, a in enumerate(A):
        carry = 0
        sum_lst = [0] * B
        for j in range(B):
            if (a >> j) & 1:
                # Aiのビットを除外
                # 次のループでもA_(i-1)の情報は要らないので永続的に1を引いてしまう
                bits[j] -= 1
                # A_(i+1)以降の0の数
                n = (N - i - 1) - bits[j]
            else:
                # A_(i+1)以降の1の数
                n = bits[j]
            assert bits[j] >= 0
            carry, sum_lst[j] = divmod(n + carry,  2)
        # (sum_lstを[0] * B で初期化していたけど、その意味が怪しくなってる)
        while carry:
            sum_lst.append(carry % 2)
            carry //= 2
        ans += sum(b * 2**j for j, b in enumerate(sum_lst))
        ans %= MOD
    print(ans)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)


if __name__ == "__main__":
    main()
