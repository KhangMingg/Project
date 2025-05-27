fi = open("bai1bt1.inp", "r")
fo = open("bai1bt1.out", "w")

sn = fi.readline().split()

a = int(sn[0])
b = int(sn[1])
c = int(sn[2])

s = (pow(a, 2) + pow(b, 2) + pow(c, 2)) * (a + b + c)
p = (a + b) * (b + c)

print(int(s), " ", p, file = fo,  )
print(f"Output: S = {int(s)}, P = {p}")