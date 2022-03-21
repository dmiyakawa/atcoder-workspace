#!/usr/bin/env python3

# 1. あなたのプログラムが、高橋君が宣言する整数として、1 以上 2N+1 以下の整数を標準出力に出力します。
#   （どちらかのプレイヤーによってすでに宣言されている整数を出力することは出来ません。）
# 2. ジャッジプログラムによって、青木君が宣言する整数があなたのプログラムに標準入力から与えられます。
#   （どちらかのプレイヤーによってすでに宣言されている整数が入力されることはありません。）
#    ただし、青木君が宣言できる整数が残っていない場合は、代わりに 0 が与えられ高橋君の勝ちでゲームが終了します。


N = int(input())

available = set(i for i in range(1, 2 * N + 2))


def put(n):
    print(n, flush=True)


def get():
    return int(input())


def main():
    put(1)
    available.discard(1)

    while available:
        available.discard(get())
        put(available.pop())
    get()
    return


if __name__ == "__main__":
    main()
