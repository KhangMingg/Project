fi  = open("bai1lua.inp", "r")
fo  = open("bai1lua.out", "w")
sn = fi.readline().split()
a = int(sn[0])
b = int(sn[1])
s = a * b
print(s, file = fo)