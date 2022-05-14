#!/usr/bin/env python3

def main():
    A, B, W_kg = [int(e) for e in input().split()]
    w = W_kg * 1000

    if B - A < (w % A) / (w // A):
        # [A, B] の範囲で重さを分配しても理論上wを分配しきれない
        print("UNSATISFIABLE")
        return
    # 分配できる前提で考えると
    # 最小数は w // B 未満になることはない
    # 最大数は w // A より多くなることはない
    print(w // B + (1 if w % B > 0 else 0), w // A)


if __name__ == "__main__":
    main()
