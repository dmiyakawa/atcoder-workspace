#!/usr/bin/env python3

def main():
    n_mul_a = 6
    n_mul_b = 5
    n_digits = [7, 6, 6, 6, 6]
    limitations = [{4: 1}, {2: 3, 4: 2}, {0: 6, 2: 5, 4: 4}, {0: 8, 2: 7}, {0: 9}]
    for a in range(10**(n_mul_a - 1), 10**n_mul_a):
        if a % 100000 == 0:
            print(a)
        b_cands = [set() for _ in range(n_mul_b)]
        for bi in range(n_mul_b):
            for digit in range(10):
                mul_result = a * digit
                if len(str(mul_result)) != n_digits[bi]:
                    continue
                ok = True
                for k, v in limitations[bi].items():
                    if (mul_result // 10**k % 10) != v:
                        ok = False
                        break
                if not ok:
                    continue
                b_cands[bi].add(digit)
                print("", bi, mul_result)
            if not b_cands[bi]:
                break
        if any(not bs for bs in b_cands):
            continue
        print(a, b_cands)
        b = 0
        lst = []
        for i, bs in enumerate(b_cands):
            bv = next(iter(bs))
            lst.append("{:>10}".format(str(a * bv) + " " * i))
            b += bv * 10**i
        print(f"{a:>10}")
        print(f"{b:>10}")
        print("----------")
        for line in lst:
            print(line)
        print(a * b)

        break


if __name__ == "__main__":
    main()
