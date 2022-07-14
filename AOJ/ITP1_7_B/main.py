def main():
    while True:
        N, X = map(int, input().split())
        if N == 0 and X == 0:
            break
        count = 0
        for a in range(1, N + 1):
            for b in range(a + 1, N + 1):
                if a + b >= X:
                    break
                c = X - a - b
                if c > N or c <= b:
                    continue
                count += 1
        print(count)


if __name__ == "__main__":
    main()
