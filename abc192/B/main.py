#!/usr/bin/env python3

def main():
    is_good = True
    for i, ch in enumerate(input(), start=1):
        if (i % 2 == 0 and ch.islower()) or (i % 2 == 1 and not ch.islower()):
            is_good = False
            break
    print("Yes" if is_good else "No")
            


if __name__ == "__main__":
    main()
