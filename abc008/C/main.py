#!/usr/bin/env python3

import sys

def solve(N: int, C: "List[int]"):

    return



def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C)





if __name__ == "__main__":
    main()
