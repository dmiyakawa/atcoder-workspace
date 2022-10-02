#!/usr/bin/env python3


def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    A = []
    for _ in range(N):
        A.extend(list(map(int, input().split())))
    assert len(A) == N**2
    m = 0
    for i in range(N**2):
        a = A[i]
        c = 0
        while a:
            c += 1
            a >>= 1
        m = max(m, c)

    oks1 = [{} for _ in range(N**2)]
    oks1[0][A[0]] = 1
    for i in range(N**2):
        h, w = divmod(i, N)
        if h + w > N - 1:
            continue
        a = A[i]
        ok = oks1[i]
        if h > 0:
            prev_ok = oks1[i - N]
            for prev_v, n in prev_ok.items():
                ok[prev_v ^ a] = ok.get(prev_v ^ a, 0) + n
        if w > 0:
            prev_ok = oks1[i - 1]
            for prev_v, n in prev_ok.items():
                ok[prev_v ^ a] = ok.get(prev_v ^ a, 0) + n

    oks2 = [{} for _ in range(N**2)]
    oks2[N**2 - 1][A[N**2 - 1]] = 1
    for i in range(N**2 - 1, -1, -1):
        h, w = divmod(i, N)
        if h + w < N - 1:
            continue
        a = A[i]
        ok = oks2[i]
        if h < N - 1:
            prev_ok = oks2[i + N]
            for prev_v, n in prev_ok.items():
                ok[prev_v ^ a] = ok.get(prev_v ^ a, 0) + n
        if w < N - 1:
            prev_ok = oks2[i + 1]
            for prev_v, n in prev_ok.items():
                ok[prev_v ^ a] = ok.get(prev_v ^ a, 0) + n
    # print(oks1)
    # print(oks2)
    ans = 0
    for h in range(N):
        w = N - 1 - h
        i = h * N + w
        if h == 0:
            for ok1, v1 in oks1[i - 1].items():
                ok2 = ok1 ^ A[i]
                if ok2 in oks2[i + N]:
                    ans += v1 * oks2[i + N][ok2]
        elif h == N - 1:
            for ok1, v1 in oks1[i - N].items():
                ok2 = ok1 ^ A[i]
                if ok2 in oks2[i + 1]:
                    ans += v1 * oks2[i + 1][ok2]
        else:
            for ok1, v1 in oks1[i - 1].items():
                ok2 = ok1 ^ A[i]
                if ok2 in oks2[i + 1]:
                    ans += v1 * oks2[i + 1][ok2]
                if ok2 in oks2[i + N]:
                    ans += v1 * oks2[i + N][ok2]
            for ok1, v1 in oks1[i - N].items():
                ok2 = ok1 ^ A[i]
                if ok2 in oks2[i + 1]:
                    ans += v1 * oks2[i + 1][ok2]
                if ok2 in oks2[i + N]:
                    ans += v1 * oks2[i + N][ok2]
    print(ans)
    # print(oks2[0].get(0, 0))





if __name__ == "__main__":
    main()
