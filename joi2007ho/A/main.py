n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

ans = sum(A[:k])
v = ans
for i in range(n - k):
    v = v - A[i] + A[i + k]
    ans = max(ans, v)
print(ans)
