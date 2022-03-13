#!/usr/bin/env python3

import math


# See also https://twitter.com/kyopro_friends/status/1502672419299164160
# > sqrtで誤差が出るのは引数がdoubleにキャストされるせいです
# > なので、doubleで正確に表すことのできない10^16前後から誤差が出ます
def sqrt_int(x) -> int:
    xx = int(math.sqrt(x) // 1)
    ans = 0
    for i in range(-1, 2):
        tmp = xx + i
        if tmp >= 0:
            if tmp * tmp <= x:
                ans = tmp
    return ans


if __name__ == "__main__":
    # しかしズレる実例が分からない
    import random
    while True:
        val = random.randrange(10 ** 16, 10 ** 16 + 10 ** 8)
        a = sqrt_int(val)
        b = int(math.sqrt(val))
        if a != b:
            print(val, a, b)
            break
