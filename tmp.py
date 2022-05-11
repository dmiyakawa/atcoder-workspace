timeT, walkT, restT, timeA, walkA, restA, jogtime = [int(e) for e in input().split()]

Ttime = jogtime - restT
walkdisT = Ttime * walkT
Atime = jogtime - restA
walkdisA = Atime * walkA

if walkdisT < walkdisA:
    print("Aoki")

elif walkdisT > walkdisA:
    print("Takahashi")

elif walkdisT == walkdisA:
    print("draw")

else:
    print("??")
