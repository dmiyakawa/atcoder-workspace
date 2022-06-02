#!/usr/bin/env python3

def main():
    N = int(input())
    rain = [0] * 288
    for _ in range(N):
        tmp = input()
        s, e = int(tmp[:2]) * 60 + int(tmp[2:4]), int(tmp[-4:-2]) * 60 + int(tmp[-2:])
        for i in range(s // 5, e // 5 + (1 if e % 5 > 0 else 0)):
            rain[i] += 1
    # print(rain)
    start = None
    for i in range(len(rain)):
        if rain[i]:
            if start is None:
                start = i * 5
        elif not rain[i]:
            if start is not None:
                end = i * 5
                start_s = f"{start // 60:02d}{start % 60:02d}"
                end_s = f"{end // 60:02d}{end % 60:02d}"
                print(f"{start_s}-{end_s}")
                start = None
    if start is not None:
        start_s = f"{start // 60:02d}{start % 60:02d}"
        end_s = "2400"
        print(f"{start_s}-{end_s}")


if __name__ == "__main__":
    main()
