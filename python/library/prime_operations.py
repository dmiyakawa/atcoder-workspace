"""
素数関連の処理をまとめる
"""


def eratosthenes(n):
    """エラトステネスのふるいの結果を[0, n)範囲のList[bool]で返す"""
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for p in range(2, n + 1):
        if not is_prime[p]:
            continue
        q = p * 2
        while q <= n:
            is_prime[q] = False
            q += p

    return is_prime
