#!/usr/bin/env python3

def main():
    x = input()
    ans = int(float(x))
    if int(x[-3]) >= 5:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
