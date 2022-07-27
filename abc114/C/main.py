#!/usr/bin/env python3


def main():
    N = int(input())
    L = 4
    combs = [(0, {"3": 0, "5": 0, "7": 0})]
    if N >= 10 ** L:
        M = N // 10 ** L
        mod_N = 10 ** L - 1
        for m in range(M + 1):
            str_m = str(m)
            if str_m.count("3") + str_m.count("5") + str_m.count("7") == len(str_m):
                combs.append((m, {"3": str_m.count("3"),
                                  "5": str_m.count("5"),
                                  "7": str_m.count("7")}))
    else:
        mod_N = N

    ans = 0
    for m, d in combs:
        for n in range(mod_N + 1):
            v = m * 10 ** L + n
            if v > N:
                break
            str_v = str(v)
            a = str_v.count("3") + str_v.count("5") + str_v.count("7") == len(str_v)
            b = str_v.count("3") and str_v.count("5") and str_v.count("7")
            if a and b:
                ans += 1
    print(ans)



if __name__ == "__main__":
    main()
