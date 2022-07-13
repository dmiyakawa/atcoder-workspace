s = input()
N = 23
ord_a = ord("A")
lst = []
for ch in s:
    lst.append(chr(((ord(ch) - ord_a) + N) % 26 + ord_a))
print("".join(lst))
