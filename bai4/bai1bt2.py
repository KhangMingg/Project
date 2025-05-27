fi = open("bai1bt2.inp", "r")
fo = open("bai1bt2.out", "w")

sn = fi.readline().split()

a = int(sn[0])
b = int(sn[1])
c = int(sn[2])

s = (a * a + b * b + c * c)*(a + b + c)
p = (a*a + b) / (b*b + c)

print(s, " ", p, file = fo,  )
print(f"Output: S = {s}, P = {p}")