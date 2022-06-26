import string

N, X = map(int, input().split())

lst = []
for ch in string.ascii_uppercase:
    lst.append(ch * N)

print("".join(lst)[X - 1])
