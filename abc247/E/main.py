#!/usr/bin/env python3

def main():
    N, X, Y = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    count = 0
    _consumed = -1
    _left = 0
    _right = 0
    _divided = 0
    while _left < N:
        do_next_round = False
        while _left < N and A[_left] not in (X, Y):
            if A[_left] < Y or X < A[_left]:
                _consumed = _left
                _left = _left + 1
                do_next_round = True
                break
            else:
                _left += 1
        if _left >= N:
            break
        if do_next_round:
            continue

        wanted = Y if A[_left] == X else X
        _right = _left

        while _right < N and A[_right] != wanted:
            if A[_right] < Y or X < A[_right]:
                _consumed = _right
                _left = _right = _right + 1
                do_next_round = True
                break
            else:
                _right += 1
        if _right >= N:
            break
        if do_next_round:
            continue

        _divided = _right + 1
        while _divided < N and Y <= A[_divided] <= X:
            _divided += 1

        new_value = (_left - _consumed) * (_divided - _right)
        count += new_value
        _consumed = _left
        _left = _right = _left + 1

    print(count)


if __name__ == "__main__":
    main()
