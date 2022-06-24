N, K, A = [int(e) for e in input().split()]
if N >= A + K - 1:
    print(A + K - 1)
else:
    K = K - (N - A + 1)
    print(K % N if K % N > 0 else N)
