#!/usr/bin/env python3


def main():
    import sys

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    T = [next(tokens) for _ in range(3)]  # type: "List[str]"
    print("Yes" if check(S, T) else "No", end="")


def check(S, T):
    if (
            (S[0], S[1], S[2]) == (T[0], T[2], T[1]) or
            (S[0], S[1], S[2]) == (T[1], T[0], T[2]) or
            (S[0], S[1], S[2]) == (T[2], T[1], T[0])
    ):
        return False
    else:
        return True


if __name__ == "__main__":
    main()
