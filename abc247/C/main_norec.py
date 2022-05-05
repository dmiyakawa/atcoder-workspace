N = int(input())

lst = [None]

for i in range(1, N + 1):
    if i == 1:
        lst.append("1")
    else:
        lst.append(lst[i - 1] + " " + str(i) + " " + lst[i - 1])

print(lst[N])
