#!/usr/bin/env python3


def main():
    T = int(input())
    for _ in range(T):
        a, s = map(int, input().split())
        ab = f"{a:060b}"  # x & y = a
        sb = f"{s:060b}"  # x + y = s
        NOT_CARRIED = 0
        POSSIBLY_CARRIED = 1
        MUST_BE_CARRIED = 2
        state = NOT_CARRIED
        no = False
        i = 0
        while i < 60:
            if state == NOT_CARRIED:
                if ab[i] == "1":
                    no = True
                    break
                if sb[i] == "1":
                    state = POSSIBLY_CARRIED
            elif state == POSSIBLY_CARRIED:
                if ab[i] == "1":
                    if sb[i] == "1":
                        state = MUST_BE_CARRIED
                    else:
                        state = NOT_CARRIED
            else:  # state == MUST_BE_CARRIED
                if ab[i] == "1":
                    if sb[i] == "0":
                        state = NOT_CARRIED
                else:
                    if sb[i] == "1":
                        no = True
                        break
            i += 1

        num_one_in_ab = ab.count("1")
        num_one_in_sb = sb.count("1")
        if state == MUST_BE_CARRIED:
            no = True

        if no:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
