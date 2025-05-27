import sys

sys.stdin = open("bai.inp", "r")
sys.stdout = open("bai.out", "w")

u = input()
a, b = map(int, u.split())

x = (a - 2) * (b - 2)

print(f"{(a - 2) * (b - 2)}") # dien tich o vuong vang
print(f"{(a * b) - ((a - 2) * (b - 2))}") # dien tich o vuong xanh
